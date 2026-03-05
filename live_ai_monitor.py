import psutil
import pandas as pd
import joblib
import time
import os

rf = joblib.load("rf_model.pkl")
anomaly = joblib.load("anomaly_model.pkl")

print("AI Threat Monitor Started")

while True:

    # system metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    processes = len(list(psutil.process_iter()))

    # network connections
    connections = psutil.net_connections(kind='inet')

    ports = set()

    for c in connections:
        if c.laddr:
            ports.add(c.laddr.port)

    unique_ports = len(ports)

    net = psutil.net_io_counters()
    ratio = net.bytes_sent / (net.bytes_recv + 1)

    # count only simulated attack files
    attack_files = len([f for f in os.listdir(".") if f.startswith("attack_file")])

    data = pd.DataFrame([{

        "failed_login_count": 0,
        "unique_ports_contacted": unique_ports,
        "dns_entropy_score": 0.3,
        "outbound_bytes_ratio": ratio,
        "restricted_access_attempts": 0,
        "unusual_process_spawn_count": processes,
        "cpu_usage": cpu,
        "memory_usage": memory,
        "file_modification_rate": attack_files

    }])

    prediction = rf.predict(data)[0]

    probability = rf.predict_proba(data)[0][1]

    anomaly_score = -anomaly.decision_function(data)[0]

    risk = (probability * 0.6) + (anomaly_score * 0.4)

    print("\n------ SYSTEM STATUS ------")
    print("CPU:", cpu)
    print("Memory:", memory)
    print("Processes:", processes)
    print("Ports:", unique_ports)
    print("Attack Files:", attack_files)

    print("Threat Probability:", round(probability,3))
    print("Risk Score:", round(risk,3))

    # balanced detection threshold
    if risk > 0.5:
        print("⚠ SUSPICIOUS ACTIVITY DETECTED")
    else:
        print("System Normal")

    time.sleep(5)
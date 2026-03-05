import subprocess
import os
import time

print("Starting attack simulation...")

# create suspicious processes
for i in range(100):
    subprocess.Popen(["cmd","/c","echo attack"])
    time.sleep(0.02)

# create many files
for i in range(300):

    with open(f"attack_file_{i}.txt","w") as f:
        f.write("attack simulation")

# CPU spike
end = time.time() + 10

while time.time() < end:
    x = 99999 ** 999

print("Attack simulation finished")
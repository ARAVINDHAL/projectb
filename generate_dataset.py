import pandas as pd
import random

data=[]

for i in range(1000):

    if random.random()<0.5:

        row=[

        random.randint(0,3),
        random.randint(1,5),
        random.uniform(0.1,0.4),
        random.uniform(0.8,1.5),
        0,
        random.randint(0,2),
        random.randint(5,20),
        random.randint(20,50),
        random.randint(0,2)

        ]

        label=0

    else:

        row=[

        random.randint(8,20),
        random.randint(30,100),
        random.uniform(0.7,1.0),
        random.uniform(3,6),
        random.randint(1,5),
        random.randint(5,15),
        random.randint(60,100),
        random.randint(60,90),
        random.randint(10,30)

        ]

        label=1

    row.append(label)
    data.append(row)

columns=[

"failed_login_count",
"unique_ports_contacted",
"dns_entropy_score",
"outbound_bytes_ratio",
"restricted_access_attempts",
"unusual_process_spawn_count",
"cpu_usage",
"memory_usage",
"file_modification_rate",
"label"

]

df=pd.DataFrame(data,columns=columns)

df.to_csv("dataset.csv",index=False)

print("Dataset created.")
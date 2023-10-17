import csv

import pandas as pd
df = pd.read_csv("data.csv")
df = df.rename(columns={"project_id" : "id","project_name" : "name","amount" : "total"})
print(df) 

csv_file = 'rename_field.csv'

with open(csv_file,mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(df)

print(f'The rename_field python file has been to {csv_file}')
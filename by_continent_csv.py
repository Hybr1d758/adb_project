import csv

import pandas as pd

data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
new_df = df[["continent","amount"]]
print(new_df)

by_continent = {}
for continent,continent_df in df.groupby("continent"):
    total_amount = continent_df["amount"].sum()
    by_continent[continent] = total_amount

for continent,total_amount in by_continent.items():
    print(f"Total amount for continent{continent}:{total_amount}")

csv_file = 'by_continent.csv'

with open(csv_file, mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(by_continent)

print(f'The by_continent python file has been written to {csv_file}')
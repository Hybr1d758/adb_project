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

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
new_df = df[["continent","amount"]]
print(new_df)

by_continent = {}
for continent,continent_df in df.groupby("continent"):
    total_amount = continent_df["amount"].sum()
    by_continent[continent] = total_amount

for continent,total_amount in by_continent.items():
    print(f"Total amount for continent {continent} : {total_amount}")



continent_axis = list(by_continent.keys())
total_amount_axis = list(by_continent.values())
colors = np.array(['red','orange','green','yellow','blue','indigo','violet'])
           
plt.xlabel("Continent")
plt.ylabel("Total amount")
plt.bar(continent_axis,total_amount_axis,color=colors)
plt.title("By_continent")
plt.show()
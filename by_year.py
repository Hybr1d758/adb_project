import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv("data.csv")


year_and_total = {}
for index, row in df.iterrows():
    "2020-03-17"

    date = row["date"]
    year = date.split("-")[0]
    amount = row["amount"]

    if year in year_and_total:
        year_and_total[year] += amount
    else:
        year_and_total[year] = amount
print(year_and_total)

year_axis = list(year_and_total.keys())
amount_axis =  list(year_and_total.values())
colors = np.array(['yellow','blue','indigo','violet'])

plt.figure(figsize=(10,6))
plt.xlabel("Year")
plt.ylabel("Amount")
plt.bar(year_axis,amount_axis, color=colors)
plt.xticks(rotation=45)
plt.title("By_year")
plt.show()



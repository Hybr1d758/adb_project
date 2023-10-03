import pandas as pd

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
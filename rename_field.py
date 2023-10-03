import pandas as pd
df = pd.read_csv("data.csv")
df = df.rename(columns={"project_id" : "id","project_name" : "name","amount" : "total"})
print(df) 
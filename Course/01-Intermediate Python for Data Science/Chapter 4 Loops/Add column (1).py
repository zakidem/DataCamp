import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

for lab, rows in cars.iterrows() :
  cars.loc[lab, "COUNTRY"] = row["country"].upper()
print(cars)

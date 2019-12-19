# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print (cars)
# Print out drives_right column as Series
print (cars.loc[:,'drives_right'])
print (cars.iloc[:,2])

# Print out drives_right column as DataFrame
print (cars.loc[:,'drives_right'])
print (cars.iloc[:,[2]])

# Print out cars_per_cap and drives_right as DataFrame
print (cars.loc[:,['cars_per_cap','drives_right']])
print (cars.iloc[:,[0,2]])

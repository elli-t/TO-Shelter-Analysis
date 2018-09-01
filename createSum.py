import pandas as pd
import numpy as np

#read in the data
df = pd.read_csv('shelter_master.csv', delimiter = ',')

#Create empty dictionaries for the occupancy and capacity 
sumOcc = dict.fromkeys(df.OCCUPANCY_DATE, 0)
sumCap = dict.fromkeys(df.OCCUPANCY_DATE, 0)

#Clean up capacity data so it's all ints/ no NaN
df.CAPACITY.fillna(0,inplace=True)
df.CAPACITY.astype(int)

#iterate through rows to sum occupancy/ capacity totals for each date 
for index, row in df.iterrows():
    x = row['OCCUPANCY']
    x +=sumOcc[row['OCCUPANCY_DATE']] 
    sumOcc[row['OCCUPANCY_DATE']] = x
    
    y = int(row['CAPACITY'])
    y +=sumCap[row['OCCUPANCY_DATE']] 
    sumCap[row['OCCUPANCY_DATE']] = y
    #print(type(row['CAPACITY']))
    

#clean dataframe up 
df2 = pd.DataFrame([sumOcc, sumCap])
df2 = df2.T
df2.columns = ['occupancy', 'capacity']
df2.index.names = ['date']
df2['% occupied'] = (df2['occupancy'] / df2['capacity']) *100


df2.to_csv('shelter_sum.csv')

print(df2.loc[df2['% occupied'] <= 90])

import pandas as pd
import numpy as np

# Display the data

zomato_data=pd.read_csv('zomato-data-analysis/Zomato data .csv')

print(zomato_data)      # he is printing the data

#display the rate column
zomato_data = zomato_data[zomato_data['rate'].str.contains(r'\d', na=False)] 
zomato_data['rate'] = zomato_data['rate'].str.split('/').str[0].astype(float) 

print(zomato_data['rate'])
print(f"the  sum of null value is {zomato_data['rate'].isnull().sum()}")

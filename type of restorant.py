import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display the data

zomato_data=pd.read_csv('zomato-data-analysis/Zomato data .csv')

# 1. Use a count plot to show the distribution of restaurant types.
plt.figure(figsize=(12, 6))  # Adjust figure size for better readability
sns.countplot(data=zomato_data, y='listed_in(type)', order=zomato_data['listed_in(type)'].value_counts().index)
plt.title('Distribution of Restaurant Types')
plt.xlabel('Number of Restaurants')
plt.ylabel('Restaurant Type')
plt.show()

# 2. Conclusion: Note which type of restaurant is the most common. Dining seems to be preferred.
most_common_type = zomato_data['listed_in(type)'].value_counts().index[0]
print(f"The most common restaurant type is: {most_common_type}")
print(f"{most_common_type} seems to be preferred.")
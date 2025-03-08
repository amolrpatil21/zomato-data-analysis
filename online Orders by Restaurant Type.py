import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


zomato_data = pd.read_csv('zomato-data-analysis/Zomato data .csv')


# 1. Create a pivot table to show the number of restaurants offering online vs. offline orders by type.
pivot_table = pd.pivot_table(zomato_data, index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)

# 2. Use a heatmap to visualize this data.
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Online vs. Offline Orders by Restaurant Type')
plt.xlabel('Online Order')
plt.ylabel('Restaurant Type')
plt.show()

# Conclusion: Note the preference of online orders for cafes and offline orders for dining restaurants.
print("Conclusion: Observe the heatmap for preferences. Generally, cafes show a preference for online orders, and dining restaurants for offline orders.")
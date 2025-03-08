import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

zomato_data = pd.read_csv('zomato-data-analysis/Zomato data .csv')


# 1. Use a count plot to examine approx_cost(for two people).

plt.figure(figsize=(15, 8))  # Adjust figure size as needed
sns.countplot(data=zomato_data, x='approx_cost(for two people)', order=zomato_data['approx_cost(for two people)'].value_counts().index)
plt.title('Distribution of Approximate Cost for Two People')
plt.xlabel('Approximate Cost (for two people)')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
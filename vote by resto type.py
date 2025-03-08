import pandas as pd

import matplotlib.pyplot as plt


zomato_data = pd.read_csv('zomato-data-analysis/Zomato data .csv')


# 1. Group the data by listed_in(type) and calculate the sum of votes.
votes_by_type = zomato_data.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)

# 2. Plot the result to show the total votes per restaurant type.
plt.figure(figsize=(10, 6))
votes_by_type.plot(kind='bar')
plt.title('Total Votes by Restaurant Type')
plt.xlabel('Restaurant Type')
plt.ylabel('Total Votes')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout() # Improves plot layout to prevent labels from being cut off.
plt.show()
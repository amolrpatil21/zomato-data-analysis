import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

zomato_data = pd.read_csv('zomato-data-analysis/Zomato data .csv')

# Clean the ratings
zomato_data = zomato_data[zomato_data['rate'].str.contains(r'\d', na=False)]
zomato_data['rate'] = zomato_data['rate'].str.split('/').str[0].astype(float)


# 1. Create a box plot to compare ratings for online vs. offline orders.

plt.figure(figsize=(8, 6))
sns.boxplot(data=zomato_data, x='online_order', y='rate')
plt.title('Ratings Comparison: Online vs. Offline Orders')
plt.xlabel('Online Order')
plt.ylabel('Rating')
plt.show()

# 2. Conclusion: Observe if online orders have higher ratings than offline ones.
online_avg = zomato_data[zomato_data['online_order'] == 'Yes']['rate'].mean()
offline_avg = zomato_data[zomato_data['online_order'] == 'No']['rate'].mean()

print(f"Average Rating for Online Orders: {online_avg:.2f}")
print(f"Average Rating for Offline Orders: {offline_avg:.2f}")

if online_avg > offline_avg:
    print("Conclusion: Online orders tend to have higher ratings than offline orders.")
elif online_avg < offline_avg:
    print("Conclusion: Offline orders tend to have higher ratings than online orders.")
else:
    print("Conclusion: Online and offline orders have similar average ratings.")
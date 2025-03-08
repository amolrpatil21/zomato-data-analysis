import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


zomato_data = pd.read_csv('zomato-data-analysis/Zomato data .csv')

# Clean the ratings
zomato_data = zomato_data[zomato_data['rate'].str.contains(r'\d', na=False)]
zomato_data['rate'] = zomato_data['rate'].str.split('/').str[0].astype(float)

# 1.) What type of restaurant do the majority of customers order from?
most_common_rest_type = zomato_data['listed_in(type)'].value_counts().index[0]
print(f"1. Majority of customers order from: {most_common_rest_type}")

# 2.) How many votes has each type of restaurant received from customers?
votes_by_rest_type = zomato_data.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)
print("\n2. Votes by Restaurant Type:")
print(votes_by_rest_type)

# 3.) What are the ratings that the majority of restaurants have received?
plt.figure(figsize=(10, 6))
plt.hist(zomato_data['rate'], bins=20, edgecolor='black')
plt.title('Distribution of Restaurant Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show() #show the histogram
print("\n3. Majority of restaurants have ratings in the range of 3.5 to 4.0 (observe histogram).")

# 4.) Zomato has observed that most couples order most of their food online. What is their average spending on each other?
online_couples = zomato_data[zomato_data['online_order'] == 'Yes']['approx_cost(for two people)'].dropna().astype(int) #convert to int.
avg_spending = online_couples.mean()
print(f"\n4. Average spending for couples ordering online: {avg_spending:.2f}")

# 5.) Which mode (online or offline) has received the maximum rating?
online_avg_rating = zomato_data[zomato_data['online_order'] == 'Yes']['rate'].mean()
offline_avg_rating = zomato_data[zomato_data['online_order'] == 'No']['rate'].mean()
if online_avg_rating > offline_avg_rating:
    print("\n5. Online mode has received the maximum rating.")
elif offline_avg_rating > online_avg_rating:
    print("\n5. Offline mode has received the maximum rating.")
else:
    print("\n5. Online and offline modes have received similar ratings.")

# 6.) Which type received more offline orders, so that Zomato can provide those customers with some good offers?
offline_orders_by_type = zomato_data[zomato_data['online_order'] == 'No']['listed_in(type)'].value_counts()
most_offline_type = offline_orders_by_type.index[0]
print(f"\n6. {most_offline_type} received the most offline orders.")
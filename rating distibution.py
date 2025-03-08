import pandas as pd
import matplotlib.pyplot as plt

# Load your Zomato data
zomato_data = pd.read_csv('zomato-data-analysis/Zomato data .csv')

# Clean the ratings
zomato_data = zomato_data[zomato_data['rate'].str.contains(r'\d', na=False)]
zomato_data['rate'] = zomato_data['rate'].str.split('/').str[0].astype(float)


# 1. Plot a histogram of the rate column to show the distribution of ratings.
plt.figure(figsize=(10, 6))
plt.hist(zomato_data['rate'], bins=20, edgecolor='black')  # Adjust bins as needed
plt.title('Distribution of Restaurant Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.6)  # Add a grid for better readability
plt.show()

# 2. Conclusion: Identify the rating range most restaurants fall into (typically 3.5 to 4).
most_common_range = (zomato_data['rate'].min(), zomato_data['rate'].max()) #initialize a range
print(f"The rating range most restaurants fall into can be observed from the histogram, but typically its 3.5 to 4.0")
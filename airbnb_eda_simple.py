
# 📊 Simple Airbnb NYC Data Analysis (With 4 Charts)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_excel("AB_NYC_2019.xlsx")

# Step 2: Basic info
print("✅ Basic Info:")
print(df.info())

# Step 3: Summary of numeric columns
print("\n✅ Summary Statistics:")
print(df.describe())

# Step 4: Correlation (numeric columns only)
corr = df.corr(numeric_only=True)
print("\n✅ Correlation with Price:")
print(corr['price'].sort_values(ascending=False))

# 🔹 Chart 1: Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap - Airbnb NYC Dataset")
plt.show()

# 🔹 Chart 2: Average Price by Neighbourhood Group
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='neighbourhood_group', y='price', estimator=pd.Series.mean, ci=None, palette='coolwarm')
plt.title("Average Price by Neighbourhood Group")
plt.ylabel("Average Price ($)")
plt.show()

# 🔹 Chart 3: Count of Listings by Room Type
plt.figure(figsize=(7,5))
sns.countplot(data=df, x='room_type', palette='Set2')
plt.title("Count of Listings by Room Type")
plt.ylabel("Number of Listings")
plt.show()

# 🔹 Chart 4: Price vs Number of Reviews
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x='number_of_reviews', y='price', alpha=0.5)
plt.title("Price vs Number of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("Price ($)")
plt.show()

print("\n🎯 Simple EDA with 4 Charts Completed Successfully!")

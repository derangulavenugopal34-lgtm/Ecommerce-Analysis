import pandas as pd

# Step 1: Read data
df = pd.read_csv("sales.csv")

# Step 2: Show data
print("Data:")
print(df)

# Step 3: Total sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Step 4: Product wise sales
product_sales = df.groupby('Product')['Sales'].sum()
print("\nProduct Sales:")
print(product_sales)
import matplotlib.pyplot as plt

product_sales.plot(kind='bar')
plt.title("Product Sales")
plt.show()
# Region wise sales
region_sales = df.groupby('Region')['Sales'].sum()
print("\nRegion Sales:")
print(region_sales)
# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Month column
df['Month'] = df['Order Date'].dt.month

# Monthly sales
monthly_sales = df.groupby('Month')['Sales'].sum()

print("\nMonthly Sales:")
print(monthly_sales)
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show()
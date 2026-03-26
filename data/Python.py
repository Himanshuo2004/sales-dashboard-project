import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/sales_data.csv')

print("Dataset Preview:")
print(df.head())

# Total Sales
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print(f"\nTotal Sales: {total_sales}")
print(f"Total Profit: {total_profit}")

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.savefig('../images/sales_by_region.png')
plt.show()

# Profit by Product
product_profit = df.groupby('Product')['Profit'].sum()

plt.figure()
product_profit.plot(kind='pie', autopct='%1.1f%%')
plt.title('Profit by Product')
plt.savefig('../images/profit_by_product.png')
plt.show()

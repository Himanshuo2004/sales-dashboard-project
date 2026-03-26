import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv('sales_data.csv')

print("Dataset Preview:")
print(df.head())

# Total Sales and Profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print(f"\nTotal Sales: {total_sales}")
print(f"Total Profit: {total_profit}")

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure()
region_sales.plot(kind='bar', color='steelblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.show()

# Profit by Product
product_profit = df.groupby('Product')['Profit'].sum()

plt.figure()
product_profit.plot(kind='pie', autopct='%1.1f%%')
plt.title('Profit by Product')
plt.tight_layout()
plt.savefig('profit_by_product.png')
plt.show()

print("\nDone! Charts saved.")

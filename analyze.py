import pandas as pd

data = {
    "Product": ["Coke", "Pepsi", "Juice", "Milk", "Biscuits"],
    "Price": [120, 115, 140, 180, 80],
    "Weight": [500, 500, 1000, 1000, 200],
    "Sugar": [53, 54, 22, 5, 18]
}

df = pd.DataFrame(data)

df["Price_per_100g"] = df["Price"] / df["Weight"] * 100

print("\nAll Products:")
print(df)

cheapest = df.loc[df["Price_per_100g"].idxmin()]
most_expensive = df.loc[df["Price_per_100g"].idxmax()]

print("\nCheapest Product (Best Value):")
print(cheapest)

print("\nMost Expensive Product (Worst Value):")
print(most_expensive)

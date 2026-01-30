import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("car.csv")
print(df.head())

plt.figure(figsize=(8,4))
sns.histplot(df["Mileage"], kde=True, bins=40)
plt.title("Mileage Distribution")
plt.xlabel("Mileage (km)")
plt.ylabel("Count")
plt.show()

brand_price = df.groupby("Brand")["Price"].mean().sort_values(ascending=False)
print(brand_price)

plt.figure(figsize=(10,4))
sns.barplot(x=brand_price.index, y=brand_price.values)
plt.title("Average Price by Brand")
plt.xticks(rotation=45)
plt.ylabel("Average Price")
plt.show()

fuel_counts = df["Fuel Type"].value_counts()
print(fuel_counts)

plt.figure(figsize=(6,4))
sns.barplot(x=fuel_counts.index, y=fuel_counts.values)
plt.title("Fuel Type Distribution")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x=df["Engine Size"], y=df["Price"])
plt.title("Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.show()

year_price = df.groupby("Year")["Price"].mean()
print(year_price)

plt.figure(figsize=(8,4))
plt.plot(year_price.index, year_price.values, marker="o")
plt.title("Average Price by Year")
plt.xlabel("Year")
plt.ylabel("Average Price")
plt.grid()
plt.show()

filtered = df[
    (df["Mileage"] < 50000) &
    (df["Year"] >= 2015) &
    (df["Transmission"] == "Automatic")
]

print(filtered)

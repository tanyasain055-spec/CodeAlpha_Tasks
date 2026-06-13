import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/games.csv")

# -------------------------
# Chart 1: Free vs Paid
# -------------------------

free_games = len(df[df["Price"] == "Free"])
paid_games = len(df[df["Price"] != "Free"])

plt.figure(figsize=(6,6))

plt.pie(
    [free_games, paid_games],
    labels=["Free", "Paid"],
    autopct="%1.1f%%"
)

plt.title("Free vs Paid Steam Games")

plt.savefig("visuals/free_vs_paid.png")
plt.close()

# -------------------------
# Chart 2: Top 10 Expensive Games
# -------------------------

top10 = df.sort_values(
    by="Clean_Price",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))

plt.bar(
    top10["Game Name"],
    top10["Clean_Price"]
)

plt.xticks(rotation=45, ha="right")

plt.title("Top 10 Most Expensive Steam Games")
plt.xlabel("Game Name")
plt.ylabel("Price")

plt.tight_layout()

plt.savefig("visuals/top10_expensive_games.png")
plt.close()

# -------------------------
# Prepare Release Year
# -------------------------

df["Year"] = (
    df["Release Date"]
    .astype(str)
    .str.extract(r'(\d{4})')
)

# -------------------------
# Chart 3: Release Year Distribution
# -------------------------

year_counts = df["Year"].value_counts().sort_index()

plt.figure(figsize=(8,5))

plt.bar(
    year_counts.index,
    year_counts.values
)

plt.title("Games Released By Year")
plt.xlabel("Year")
plt.ylabel("Number of Games")

plt.savefig("visuals/release_year_distribution.png")
plt.close()

# -------------------------
# Chart 4: Price Distribution
# -------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df["Clean_Price"].dropna(),
    bins=10
)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.savefig("visuals/price_distribution.png")
plt.close()

print("All charts generated successfully!")

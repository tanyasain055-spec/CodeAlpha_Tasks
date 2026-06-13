import pandas as pd

df = pd.read_csv("data/games.csv")

print("========== DATASET OVERVIEW ==========")

print("\nTotal Games:", len(df))

print("\nAverage Price:")
print(df["Clean_Price"].mean())

free_games = len(df[df["Price"] == "Free"])
paid_games = len(df[df["Price"] != "Free"])

print("\nFree Games:", free_games)
print("Paid Games:", paid_games)

print("\nTop 5 Most Expensive Games:")
print(
    df.sort_values(
        by="Clean_Price",
        ascending=False
    )[["Game Name", "Price"]].head()
)

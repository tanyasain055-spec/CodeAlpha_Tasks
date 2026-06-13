import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://store.steampowered.com/search/?filter=topsellers"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Scrape data
titles = soup.find_all("span", class_="title")
prices = soup.find_all("div", class_="discount_final_price")
release_dates = soup.find_all("div", class_="search_released")

# Check counts
print("Titles:", len(titles))
print("Prices:", len(prices))
print("Dates:", len(release_dates))

# Create dataset
games = []

for title, price, date in zip(titles, prices, release_dates):
    games.append([
        title.text.strip(),
        price.text.strip(),
        date.text.strip()
    ])

# DataFrame
df = pd.DataFrame(
    games,
    columns=["Game Name", "Price", "Release Date"]
)

# Clean price column
df["Clean_Price"] = df["Price"].replace("Free", "0")

df["Clean_Price"] = (
    df["Clean_Price"]
    .str.replace("$", "", regex=False)
    .str.replace("¥", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Clean_Price"] = pd.to_numeric(
    df["Clean_Price"],
    errors="coerce"
)

# Preview
print(df.head())
print(df.shape)

# Save CSV
df.to_csv("data/games.csv", index=False)

print("CSV file created successfully!")
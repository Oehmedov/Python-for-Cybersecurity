import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# Amazon product URL
URL = "https://www.amazon.com/dp/B074473Z6T"

# Headers to mimic a real browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

def get_price():
    """Fetches product title and price from Amazon"""
    response = requests.get(URL, headers=HEADERS)

    if response.status_code != 200:
        print("Failed to fetch page")
        return None, None

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find(id="productTitle")
    price = soup.find("span", class_="a-offscreen")

    if not title or not price:
        print("Price or title not found")
        return None, None

    title_text = title.get_text(strip=True)
    price_text = price.get_text(strip=True)

    return title_text, price_text


def track_price():
    title, price = get_price()

    if title and price:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] {title}")
        print(f"Current Price: {price}\n")

        # Save to file
        with open("price_log.txt", "a", encoding="utf-8") as file:
            file.write(f"{now} | {title} | {price}\n")


if __name__ == "__main__":
    print("Amazon Price Tracker Started...\n")

    while True:
        track_price()
        time.sleep(3600)  # check every 1 hour
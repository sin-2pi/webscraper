from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.remax.com/homes-for-sale/wy/laramie/city/5645050")

soup = BeautifulSoup(response.text, "lxml")

priceLimit = input("What is your price limit? ")
priceLimit = int(priceLimit.replace("$", "").replace(",", ""))

prices = soup.find_all("h4", class_="d-listing-card-price")
locations = soup.find_all("h3", class_="d-listing-card-address-link")

for price, location in zip(prices, locations):
    price_text = price.text.strip()
    price_int = int(price_text.replace("$", "").replace(",", ""))
    location_text = location.text.strip()

    if price_int <= priceLimit:
        print(
            f"""
        Price: {price_text} (${price_int})
        Location: {location_text}
            """
        )

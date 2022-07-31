import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.de/-/en/Samsung-Android-Smartphone-Contract-including/dp/B09QH3B75W/ref=sr_1_3?keywords=samsung%2Bgalaxy%2Bs22%2Bultra&qid=1659289761&sprefix=samsun%2Caps%2C148&sr=8-3&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


# Retrieve Amazon product page and check if price is below or at target price
def check_price(target_price):

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ----------------------------------------------------------------
    title = soup.find(id="productTitle").get_text()
    price = float(soup.find(class_="a-price-whole").get_text().strip(".").replace(",", ""))

    if price <= target_price:
        send_email()

# Send email informing you of the price of the product
def send_email():
    pass
    #TODO

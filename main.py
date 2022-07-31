import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.de/-/en/Samsung-Android-Smartphone-Contract-including/dp/B09QH3B75W/ref=sr_1_3?keywords=samsung%2Bgalaxy%2Bs22%2Bultra&qid=1659289761&sprefix=samsun%2Caps%2C148&sr=8-3&th=1"
FROM_ADDRESS = "" # Add sender here
TO_ADDRESSES = [] # Add recipients here

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


# Retrieve Amazon product page and check if price is below or at target price
def check_price(target_price):

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ----------------------------------------------------------------
    title = soup.find(id="productTitle").get_text()
    currency = soup.find(class_="a-price-symbol").get_text()
    price = soup.find(class_="a-price-whole").get_text().strip(". ")

    float_price = float(price.replace(",", ""))

    if float_price <= target_price:
        send_email(title, currency, price, target_price)
    else:
        print("Price is higher than the target price: no email will be sent.")

# Send email informing you of the price of the product
def send_email(title, currency, price, target_price):
    server = smtplib.SMTP('smtp.gmail.com', port=587)

    server.ehlo() # 'Extended Hello': Command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.
    server.starttls() # If the server supports TLS, this will encrypt the rest of the SMTP session.
    server.ehlo() 

    server.login(FROM_ADDRESS, "") # Email | Password

    subject = "Amazon alert: price fell down!"
    body = f"""
            The price for one of the products on your wishlist fell to {currency}{price}!
            You had set a target price of {currency}{target_price}.
            
            Check the Amazon product page here: {URL}

            Get it before this price drop ends!"""

    msg = f"Subject: {subject}\n\n{body}"


    server.sendmail(
        FROM_ADDRESS,
        TO_ADDRESSES,
        msg.encode("utf-8")
    )
    print("Email has been successfully sent!")

    server.quit() # Terminates the SMTP session.


# Test scenario
check_price(1400)



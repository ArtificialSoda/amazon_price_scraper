import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.ca/Samsung-Standard-Dual-SIM-Factory-Unlocked/dp/B09NRT43TM/ref=sr_1_8?keywords=samsung+s22&qid=1659285580&sr=8-8"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
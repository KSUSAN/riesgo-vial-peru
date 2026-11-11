import requests
from bs4 import BeautifulSoup

url = "https://www.gob.pe"

response = requests.get(url)

print(
    f"Status: {response.status_code}"
)

print(
    "Web Scraping ejecutado"
)

import requests
from bs4 import BeautifulSoup
import random

class WebScraper:
    def __init__(self, url):
        self.url = url

        # basic user-agent rotation
        self.headers_list = [
            {"User-Agent": "Mozilla/5.0"},
            {"User-Agent": "Chrome/100.0"},
            {"User-Agent": "Safari/537.36"}
        ]

    def get_html(self):
        headers = random.choice(self.headers_list)
        response = requests.get(self.url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            print("❌ Failed to fetch page")
            return None

    def scrape_titles(self):
        html = self.get_html()
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")

        # example: get all headings
        titles = soup.find_all("h2")

        print("\n🌐 Scraped Titles:\n")
        for i, title in enumerate(titles[:10], start=1):
            print(f"{i}. {title.get_text(strip=True)}")
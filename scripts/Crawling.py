import requests
import warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from urllib.parse import urljoin, urlsplit


class Crawling:
    def __init__(self, url):
        self.url = url

    def crawling(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
        try:
            print("Crawling...")
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            req = requests.get(self.url, headers=headers, allow_redirects=False, timeout=5).text
            soup = BeautifulSoup(req, 'html.parser')
            read_wordlist = open("./db/admin.txt", encoding='utf-8').read().splitlines()
            for word_path in read_wordlist:
                for path in soup.find_all('a'):
                    path_href = urlsplit(path['href']).path
                    if word_path == path_href:
                        print(f"Found: {word_path}")
            return True
        except:
            pass
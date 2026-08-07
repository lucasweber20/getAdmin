import requests
import warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from urllib.parse import urljoin, urlsplit


class Crawling:
    def __init__(self, body, url):
        self.body = body
        self.url = url

    def crawling(self):
        urls = []
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
        try:
            print("Crawling...")
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            tags = ["a", "link", "area", "base"]
            attrs = ["href"]
            soup = BeautifulSoup(self.body, 'html.parser')
            read_wordlist = open("./db/admin.txt", encoding='utf-8').read().splitlines()
            for word_path in read_wordlist:
                for path in soup.find_all(tags):
                    for attr in attrs:
                        path_href = urlsplit(path[attr]).path
                        if word_path == path_href:
                            urls.append(self.url)
            return urls
        except:
            pass
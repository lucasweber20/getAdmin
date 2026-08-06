import requests


class Crawling:
    def __init__(self, url):
        self.url = url

    def crawling(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
        try:
            print("Crawling...")
            req = requests.get(self.url, headers=headers, allow_redirects=False, timeout=5).text
            read_wordlist = open("./db/admin.txt", encoding='utf-8').read().splitlines()
            for path in read_wordlist:
                if path in req:
                    print(f"Found: {path}")
            return True
        except:
            pass
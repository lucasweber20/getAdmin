from os.path import splitext
from urllib.parse import urlsplit


class Parser:
    def __init__(self, url):
        self.url = url

    def blacklist_ext(self):
        blacklist_ext = [".css", ".pdf", ".jpg", ".png", ".svg"]
        _, url_extension = splitext(self.url)
        if url_extension in blacklist_ext:
            return False
        else:
            return True

    def parser_url(self):
        parsed_urls = []
        read_wordlist = open("./db/admin.txt", encoding='utf-8').read().splitlines()
        for url in self.url:
            scheme = urlsplit(url).scheme
            hostname = urlsplit(url).netloc
            for path in read_wordlist:
                parser_url = f"{scheme}://{hostname}{path}"
                parsed_urls.append(parser_url)
        result = list(dict.fromkeys(parsed_urls))
        return result
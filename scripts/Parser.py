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
import os
from urllib.parse import urlsplit
from scripts.Parser import Parser


class Search:
    def __init__(self, urls):
        self.urls = urls

    def search_admin(self):
        result = []
        read_wordlist = open("./db/admin.txt", encoding='utf-8').read().splitlines()
        for url in self.urls:
            parser = Parser(url)
            parsed_url = parser.blacklist_ext()
            if parsed_url:
                path_url = urlsplit(url).path.split("/")
                for path in path_url:
                    format_path = f"/{path}"
                    for path_word in read_wordlist:
                        if path_word == format_path:
                            result.append(url)
        return result
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
                for path in read_wordlist:
                    if path in url:
                        result.append(url)
        return result
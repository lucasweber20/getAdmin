from scripts.Parser import Parser


class Search:
    def __init__(self, urls):
        self.urls = urls

    def search_admin(self):
        result = []
        keyword = "admin"
        for url in self.urls:
            parser = Parser(url)
            parsed_url = parser.blacklist_ext()
            if parsed_url:
                if keyword in url:
                    result.append(url)
        return result
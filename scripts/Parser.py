from os.path import splitext


class Parser:
    def __init__(self, url):
        self.url = url

    def parser_url(self):
        pass

    def blacklist_ext(self):
        blacklist_ext = [".css", ".pdf", ".jpg", ".png", ".svg"]
        _, url_extension = splitext(self.url)
        if url_extension in blacklist_ext:
            return False
        else:
            return True

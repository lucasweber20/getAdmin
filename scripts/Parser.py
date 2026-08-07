from os.path import splitext


class Parser:
    def __init__(self, url):
        self.url = url

    def blacklist_ext(self):
        blacklist_ext = [".js", ".css", ".pdf", ".jpg", ".png", ".jpeg", ".svg", ".ico", ".eot", ".ttf", ".woff", ".woff2"]
        _, url_extension = splitext(self.url)
        if url_extension in blacklist_ext:
            return False
        else:
            return True
from os.path import splitext


class Parser:
    def __init__(self, url):
        self.url = url

    def blacklist_ext(self):
        blacklist_ext = [".js", ".css", ".pdf", ".PDF", ".jpg", ".JPG", ".png", ".jpeg", ".svg", ".ico", ".gif", 
                         ".eot", ".webp", ".ttf", ".woff", ".woff2"]
        _, url_extension = splitext(self.url)
        if url_extension in blacklist_ext or "?v=" in self.url\
            or "?ver=" in self.url:
            return False
        else:
            return True
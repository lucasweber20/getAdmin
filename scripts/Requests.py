import requests


class Requests:
    def __init__(self):
        pass

    def requests(self, url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
        try:
            req = requests.get(url, headers=headers, allow_redirects=False, timeout=5)
            url_request = req.url
            status_code = req.status_code
            length = len(req.content)
            return url_request, status_code, length
        except:
            pass

    def exclude_length(self, length, exclude_length):
        if exclude_length == str(length):
            return False
        elif "," in exclude_length:
            for lengths in exclude_length.split(','):
                if lengths == str(length):
                    return False
        
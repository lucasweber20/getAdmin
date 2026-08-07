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
            body = req.text
            location = req.headers.get("Location")
            return url_request, status_code, body, location
        except:
            pass
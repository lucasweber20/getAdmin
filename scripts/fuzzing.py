import concurrent.futures
from scripts.Requests import Requests


class Fuzzing:
    def __init__(self, url):
        self.url = url

    def fuzzing(self, thread):
        req = Requests()
        with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
            futures = [executor.submit(req.requests, url) for url in self.url]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result[1] >= 200 and result[1] < 300:
                    print(f"{result[0]} -> \033[92m{result[1]}\033[00m Length: [{result[2]}]")
                elif result[1] >= 300 and result[1] < 400:
                    print(f"{result[0]} -> \033[36m{result[1]}\033[00m Length: [{result[2]}]")
                elif result[1] >= 400 and result[1] < 500:
                    print(f"{result[0]} -> \033[33m{result[1]}\033[00m Length: [{result[2]}]")
                elif result[1] >= 500 and result[1] < 600:
                    print(f"{result[0]} -> \033[31m{result[1]}\033[00m Length: [{result[2]}]")
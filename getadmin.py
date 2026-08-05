import argparse
import concurrent.futures
from scripts.URL import URL
from scripts.Search import Search
from scripts.Requests import Requests


parser = argparse.ArgumentParser()

args = parser.add_argument("-l", "--list", help="Specify file with urls, example: -l urls.txt", type=str)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)

args = parser.parse_args()

def main():
    # Flags
    file = args.list
    output = args.output

    urls = URL(file)

    # Remove duplicates
    url = urls.remove_duplicates()

    # Search admin path
    search = Search(url)
    admin_urls = search.search_admin()

    # Requests
    req = Requests()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(req.requests, url) for url in admin_urls]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result[1] >= 200 and result[1] < 300:
                print(f"{result[0]} -> \033[92m{result[1]}\033[00m")
            elif result[1] >= 300 and result[1] < 400:
                print(f"{result[0]} -> \033[36m{result[1]}\033[00m")
            elif result[1] >= 400 and result[1] < 500:
                print(f"{result[0]} -> \033[33m{result[1]}\033[00m")
            elif result[1] >= 500 and result[1] < 600:
                print(f"{result[0]} -> \033[31m{result[1]}\033[00m")
            if output:
                write_file = open(output, "a").write(f"{result[0]} -> {result[1]}\n")

if __name__ == "__main__":
    main()
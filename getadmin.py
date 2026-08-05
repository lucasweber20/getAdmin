import argparse
from scripts.URL import URL


parser = argparse.ArgumentParser()

args = parser.add_argument("-u", "--url", help='Specify url, example: -u https://example.com/?param=value', nargs="+", type=str)
args = parser.add_argument("-l", "--list", help="Specify file with urls, example: -l urls.txt", type=str)

args = parser.parse_args()

def main():
    # Flags
    url = args.url
    file = args.list

    urls = URL(url, file)

    # Remove duplicates
    if file:
        url = urls.remove_duplicates()

if __name__ == "__main__":
    main()
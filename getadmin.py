import argparse
from scripts.URL import URL
from scripts.Search import Search


parser = argparse.ArgumentParser()

args = parser.add_argument("-l", "--list", help="Specify file with urls, example: -l urls.txt", type=str)

args = parser.parse_args()

def main():
    # Flags
    file = args.list

    urls = URL(file)

    # Remove duplicates
    url = urls.remove_duplicates()

    # Search admin path
    search = Search(url)
    result = search.search_admin()

if __name__ == "__main__":
    main()
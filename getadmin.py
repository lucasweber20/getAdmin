import argparse


parser = argparse.ArgumentParser()

args = parser.add_argument("-l", "--list", help="Specify file with urls, example: -l urls.txt", type=str)

args = parser.parse_args()

def main():
    file = args.list

if __name__ == "__main__":
    main()
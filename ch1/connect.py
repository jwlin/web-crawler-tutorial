import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get('https://tw.yahoo.com/')
    print(resp.text)


if __name__ == '__main__':
    main()
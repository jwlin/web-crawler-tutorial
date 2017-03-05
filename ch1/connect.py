import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup.find('h1').text)


if __name__ == '__main__':
    main()

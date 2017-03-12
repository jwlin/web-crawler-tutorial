import requests
import re
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 找出所有 'h' 開頭的標題文字
    titles = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for title in titles:
        print(title.text.strip())

    # 利用 regex 找出所有 'h' 開頭的標題文字
    for title in soup.find_all(re.compile('h[1-6]')):
        print(title.text.strip())

    # 找出所有 .png 結尾的圖片
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if img['src'].endswith('.png'):
                print(img['src'])

    # 利用 regex 找出所有 .png 結尾的圖片
    for img in soup.find_all('img', {'src': re.compile('.png$')}):
        print(img['src'])

    # 找出所有 .png 結尾且含 'beginner' 的圖片
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if 'beginner' in img['src'] and img['src'].endswith('.png'):
                print(img['src'])

    # 利用 regex 找出所有 .png 結尾且含 'beginner' 的圖片
    for img in soup.find_all('img', {'src': re.compile('crawler.*\.png$')}):
        print(img['src'])


if __name__ == '__main__':
    main()

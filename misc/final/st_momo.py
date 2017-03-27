import urllib.parse
from bs4 import BeautifulSoup

import requests


def st_momo(query, low_price=-1, high_price=-1):
    query_enc = urllib.parse.quote(query)
    url = "http://m.momoshop.com.tw/mosearch/" + query_enc + ".html"
    headers = {'User-Agent': 'mozilla/5.0 (Linux; Android 6.0.1; '
                             'Nexus 5x build/mtc19t applewebkit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2702.81 Mobile Safari/537.36'}
    print(url)
    req = requests.get(url, headers=headers)
    if req is None:
        return []
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')
    elems = soup.select("div.directoryPrdListArea ul li")

    item_list = []

    for elem in elems:
        item_name = elem.contents[1].text
        item_price_str = elem.find("b", class_="price").text.replace(",", "")

        if not item_price_str:
            continue
        item_price = int(item_price_str)
        # print item_price

        base_url = "http://m.momoshop.com.tw"
        href = elem.find('a')['href']
        item_url = base_url + href
        # print item_url

        item_img_url = elem.contents[1].contents[0].get('org', '')

        item = dict()
        item['name'] = item_name
        item['price'] = item_price
        item['url'] = item_url
        item['img_url'] = item_img_url
        item['store'] = 'momo'
        item_list.append(item)

    return item_list


def main():
    item_list = st_momo('iphone 7')
    print('len(item_list) = ', len(item_list))
    for item in item_list:
        print(item)


if __name__ == "__main__":
    main()

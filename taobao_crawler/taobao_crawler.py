import urllib
import requests
from requests.adapters import HTTPAdapter

base_url = 'https://world.taobao.com/search/json.htm?q='


def crawl_taobao(query):
    try:
        query_enc = urllib.parse.quote(query)
    except TypeError:
        return []
    url = base_url + query_enc
    response = request_url(url)
    if response is None:
        print ('Error: response is None. url=', url)
        return []

    item_list = parse_items_from_json(response.json())
    return item_list


def parse_items_from_json(json_dict):
    item_list = list()
    item_objects = json_dict['itemList']
    for item_obj in item_objects:
        item = dict()
        item['name'] = item_obj['tip']
        item['price'] = int(float(item_obj['priceWap']))
        item['img_url'] = 'http:' + item_obj['image']
        item['url'] = 'http:' + item_obj['href']
        item['store'] = 'taobao'
        item_list.append(item)
    return item_list


def request_url(url, timeout=3, max_retries=3):
    s = requests.Session()
    s.mount(url, HTTPAdapter(max_retries=max_retries))
    try:
        response = s.get(url, timeout=timeout)
    except requests.exceptions.RequestException as e:
        print (e)
        return None

    return response


def main():
    item_list = crawl_taobao("htc re")
    for item in item_list:
        print (item)


if __name__ == '__main__':
    main()

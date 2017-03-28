import html
import urllib.parse
import time
import json
import requests
import os
from requests.adapters import HTTPAdapter


def get_resp(url, timeout=3, max_retries=3):
    # 3 秒未回應即為失敗, 最多失敗 3 次
    s = requests.Session()
    s.mount(url, HTTPAdapter(max_retries=max_retries))
    try:
        resp = s.get(url, timeout=timeout)
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    return resp


def search_pchome(query):
    query = urllib.parse.quote(query)
    # &price=10000-40000: 鎖定價格帶 10000-40000
    query_url = "http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + query + "&sort=rnk&price=10000-40000"
    resp = get_resp(query_url)
    if not resp:
        return []

    resp.encoding = 'utf-8'
    data = resp.json()  # 直接將 response 轉為 json
    if data['prods'] is None:
        return []

    total_page_count = int(data['totalPage'])
    if total_page_count == 1:
        return get_items(data)

    # 若不只一頁, 則取得各頁 url 再依序取得各頁的物件
    urls = []
    cur_page = 1
    while cur_page <= total_page_count:
        cur_page_url = query_url + '&page=' + str(cur_page)
        urls.append(cur_page_url)
        cur_page += 1
    items = []
    for url in urls:
        resp = get_resp(url)
        if resp:
            resp.encoding = 'utf-8'
            items += get_items(resp.json())
    return items


def get_items(json_dict):
    item_list = list()
    item_objects = json_dict['prods']
    for item_obj in item_objects:
        try:
            item = dict()
            item['name'] = html.unescape(item_obj['name'])
            item['price'] = int(item_obj['price'])
            item['describe'] = item_obj['describe']
            item['img_url'] = 'http://ec1img.pchome.com.tw/' + item_obj['picB']
            item['url'] = 'http://24h.pchome.com.tw/prod/' + item_obj['Id']
            item_list.append(item)
        except Exception:
            pass
    return item_list


if __name__ == '__main__':
    query = 'iphone 7 128g plus'
    items = search_pchome(query)
    today = time.strftime('%m-%d')
    print('%s 搜尋 %s 共 %d 筆資料' % (today, query, len(items)))
    for i in items:
        print(i)
    data = {
        'date': today,
        'store': 'pchome',
        'items': items
    }
    with open(os.path.join('json', today + '-pchome.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

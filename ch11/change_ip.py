from bs4 import BeautifulSoup
import requests
import random

if __name__ == '__main__':
    proxy_ips = ['121.40.199.105:80', '122.49.35.168:33128']
    ip = random.choice(proxy_ips)
    print('Use', ip)
    resp = requests.get('http://whatismyip.org/', proxies={'http': 'http://' + ip})
    soup = BeautifulSoup(resp.text, 'html5lib')
    print(soup.find_all('div')[1].span.text.strip())

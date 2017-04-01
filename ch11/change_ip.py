from bs4 import BeautifulSoup
import requests
import random

if __name__ == '__main__':
    proxy_ips = ['111.241.103.87:8888', '118.99.178.21:8080']
    ip = random.choice(proxy_ips)
    print('Use', ip)
    resp = requests.get('http://whatismyip.org/', proxies={'http': 'http://' + ip})
    soup = BeautifulSoup(resp.text, 'html5lib')
    print(soup.find_all('div')[1].text.replace('\n', '').strip())

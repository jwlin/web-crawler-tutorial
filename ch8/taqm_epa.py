import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    URL = 'https://taqm.epa.gov.tw/taqm/tw/HourlyData.aspx'
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, 'html5lib')
    view_state = soup.find(id='__VIEWSTATE')['value']
    event_validation = soup.find(id='__EVENTVALIDATION')['value']
    viewstate_generator = soup.find(id='__VIEWSTATEGENERATOR')['value']
    form_data = {
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': viewstate_generator,
        '__EVENTVALIDATION': event_validation,
        'ctl04$lbSite': '56',
        'ctl04$lbParam': '4',
        'ctl04$txtDateS': '2018/05/01',
        'ctl04$txtDateE': '2018/05/31',
        'ctl04$btnQuery': '查詢即時值'
    }
    resp = requests.post(URL, data=form_data)
    soup = BeautifulSoup(resp.text, 'html5lib')
    for t in soup.find_all('table', 'TABLE_G'):
        print([s for s in t.stripped_strings])

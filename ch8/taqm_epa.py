import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    resp = requests.get('http://taqm.epa.gov.tw/taqm/tw/HourlyData.aspx')
    soup = BeautifulSoup(resp.text, 'html5lib')
    view_state = soup.find(id='__VIEWSTATE')['value']
    event_validation = soup.find(id='__EVENTVALIDATION')['value']
    viewstate_generator = soup.find(id='__VIEWSTATEGENERATOR')['value']
    form_data = {
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': viewstate_generator,
        '__EVENTVALIDATION': event_validation,
        'ctl09$lbSite': '56',
        'ctl09$lbParam': '4',
        'ctl09$txtDateS': '2017/02/01',
        'ctl09$txtDateE': '2017/03/31',
        'ctl09$btnQuery': '查詢即時值'
    }
    resp = requests.post('http://taqm.epa.gov.tw/taqm/tw/HourlyData.aspx', data=form_data)
    soup = BeautifulSoup(resp.text, 'html5lib')
    for t in soup.find_all('table', 'TABLE_G'):
        print([s for s in t.stripped_strings])

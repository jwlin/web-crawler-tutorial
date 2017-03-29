import requests

ACCESS_TOKEN = ''
page_id = 1707015819625206  # Pycone 松果城市粉絲專頁 id


def get_me_friends():
    url = 'https://graph.facebook.com/v2.8/me?fields=id,name,friends&access_token={}'.format(ACCESS_TOKEN)
    data = requests.get(url).json()
    print('My ID:', data['id'])
    print('My name:', data['name'])
    print('I have', data['friends']['summary']['total_count'], 'friends')


def get_page_post():
    url = 'https://graph.facebook.com/v2.8/{0}/posts?access_token={1}'.format(page_id, ACCESS_TOKEN)
    data = requests.get(url).json()
    print('粉絲頁有', len(data['data']), '篇貼文')
    print('最新一篇時間:', data['data'][0]['created_time'])
    print('內容:', data['data'][0]['message'])


if __name__ == '__main__':
    get_me_friends()
    get_page_post()

import requests
import json

ACCESS_TOKEN = ''
page_id = 1707015819625206

url = 'https://graph.facebook.com/v2.8/{0}/posts?access_token={1}'.format(page_id, ACCESS_TOKEN)

res = requests.get(url)
page_posts = json.loads(res.text)
for post in page_posts['data']:
    try:
        print ('post_id: {0}, post_created_time: {1}, post_message: {2}'.format(post['id'], post['created_time'], post['message']))
    except Exception:
        print ('post_id: {0}, post_created_time: {1}'.format(post['id'], post['created_time']))

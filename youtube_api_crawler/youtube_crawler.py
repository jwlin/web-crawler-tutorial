# requests module
import requests

# python standard libs
import json
import re


class YoutubeCrawler(object):
    def __init__(self):
        self.key = ''
        self.url = 'https://www.googleapis.com/youtube/v3/search'
        self.part = 'snippet'

    def crawl_search_result(self, query):
        query = query + ' mv'
        url = '{0}?key={1}&part={2}&q={3}'.format(
            self.url, self.key, self.part, query)
        r = requests.get(url)
        r_json = json.loads(r.text)
        mvs = []
        for i, r in enumerate(r_json['items']):
            mv = {}
            mv['youtube_id'] = r['id']['videoId']
            mv['youtube_link'] = 'https://www.youtube.com/watch?v=' + \
                mv['youtube_id']
            mv['youtube_publishedAt'] = self.change_time_format(r['snippet']['publishedAt'])
            mv['youtube_title'] = r['snippet']['title']
            mv['youtube_description'] = r['snippet']['description']
            mvs.append(mv)
        for mv in mvs:
            print('song: {0}, youtube link: {1}'.format(mv['youtube_title'], mv['youtube_link']))
        return mvs

    def change_time_format(self, publishedAt):
        pat_time = '\d+-\d+-\d+'
        match = re.search(pat_time, publishedAt)
        if match is None:
            return publishedAt
        else:
            return match.group(0)


def main():
    yc = YoutubeCrawler()
    yc.crawl_search_result('gun n roses')


if __name__ == '__main__':
    main()

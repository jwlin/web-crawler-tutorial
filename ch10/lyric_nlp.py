import json
import jieba
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud


jieba.set_dictionary('dict.txt.big')  # 對繁體中文斷詞較準確的字典檔


def jieba_test():
    s = 'Python是非常強的的程式語言, 簡潔友好的語法特別容易上手, 又有許多第三方函式庫的支援。 ' \
        'Python是完全物件導向的語言, 有益於減少程式碼的重複性。' \
        'Python的設計哲學是優雅, 明確, 簡單。 Python的設計風格, 使其成為易讀, 易維護且具有廣泛用途的程式語言。'
    print([seg for seg in jieba.cut(s)])


def lyrics():
    with open('lyrics.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    tokens = list()
    for v in data.values():
        # 斷詞後的結果, 若非空白且長度為 2 以上, 則列入詞庫
        tokens += [seg for seg in jieba.cut(v) if seg.split() and len(seg) > 1]

    # 計算 tokens 內各詞彙的出現次數
    counter = Counter(tokens)
    print(counter.most_common(10))

    # 文字雲, 要顯示中文需附上字型檔
    wcloud = WordCloud(font_path='NotoSansMonoCJKtc-Regular.otf').generate(' '.join(tokens))
    plt.imshow(wcloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    jieba_test()
    lyrics()

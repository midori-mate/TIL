# !/usr/bin/env python
# coding: utf-8

# ==============================
# feedparserをインストールする
#     Python34/Scripts cmdで "pip install feedparser"
# ==============================
import feedparser
url = "http://blog.livedoor.jp/coleblog/index.rdf"
response = feedparser.parse(url)    # <class 'feedparser.FeedParserDict'>

print(response.feed.title)  # サイトタイトル
print(response.feed.link)   # サイトurl

for entry in response.entries:
    title   = entry.title      # 記事タイトル
    link    = entry.link       # 記事リンク
    updated = entry.updated    # 記事日時
    print(title, link, updated)


# ==============================
# ブラウザを開く
# ==============================
import webbrowser

url = "http://guild-elf.jugem.jp/"
webbrowser.open(url)




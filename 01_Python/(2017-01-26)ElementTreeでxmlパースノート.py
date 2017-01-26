# coding: utf-8

'''xml.etree.ElementTreeノート
xml例:mrrhpの記事xml
xmlをchromeで見ながらやるとわかりやすい。
'''

from xml.etree.ElementTree import *

# ファイルからの場合
xmlname = 'jugem8.xml'
tree = parse(xmlname) # xml.etree.ElementTree.ElementTree object
root = tree.getroot() # Element 'blog'

# 子要素の見方 rootの下には何がある?
for r in root:
    r.tag # name description users entries

# さらに子要素 usersの下には何がある?
users = root.find('users')
for u in users:
    u.tag # user user user user user

# さらに子要素 userの下には何がある?
first_user = users.find('user')
for f in first_user:
    f.tag  # name full_name description
    f.text # niconico-pon 緑色 ■ニックネーム<br />■年齢<br />...

# userをリストでとりたい
user_list = users.findall('user')
for l in user_list:
    l # <Element 'user' at 0x106e7b5e8>(user1のuser) <Element 'user' at 0x106e8ddb8>(user2のuser)...

# 例題:エントリタイトルの一覧を出力
#     タイトルの位置はblog(root)-entries-entry-title
entries = root.find('entries')
entry_list = entries.findall('entry')
for entry in entry_list:
    print(entry.find('title').text)
    # 以上ッ!





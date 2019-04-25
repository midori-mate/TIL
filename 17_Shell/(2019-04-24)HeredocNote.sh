#!/bin/sh

# 
# ヒアドキュメントノート HeredocNote
# 
# Vagrantfile -> provision.sh のときに、
#     1. テキストファイルを作りたかったり、
#     2. mysql のコマンドを実行したかったりした。
# それに応える。
# 

# ファイルを作る。
cat << __EOF__ > ./test.txt
内容
内容
__EOF__

# > をふたつにすると追記。
cat << __EOF__ >> ./test.txt
内容
内容
__EOF__

# MySQL のコマンドを実行。パスワードが password の場合。
mysql -u root -ppassword << __EOF__
SET character_set_database=utf8;
SET character_set_server=utf8;
CREATE DATABASE app;
__EOF__

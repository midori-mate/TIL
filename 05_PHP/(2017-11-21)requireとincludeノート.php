<?php

# require: ファイル読み込み失敗したら、そこで Fatal エラーになる。
// require 'ph3.php';

# include: ファイル読み込み失敗しても、Warningが出るだけで続行する。
// include 'ph3.php';

# require_once: requireと同じ挙動。ただし二回目のrequire_onceは無視される。エラーも出ない(なんでやねんエラーでろや)。
# 個人的にはこれをクラスとか関数の読み込みに使いたい。
// require_once 'ph.php';
// require_once 'ph.php';

# include_once: includeと同じ挙動。ただし二回目については無視される。エラーも出ない。
// include_once 'ph.php';
// include_once 'ph.php';

# 読み込み失敗しても続行してるのか確かめるecho。
echo 'でえええええええええええ';

<?php

/**
 * analyticsAPI調査メモ
 * クエリとその結果例を並べる。
 * このノートのクエリには書いてないけど、クエリにはviewを含めること!
 */

# 全セッション数
$query = [
    'startdate' => '2016-08-01',
    'enddate'   => 'today',
    'metrics'   => 'ga:sessions',
    'options' => [
        'dimensions'  => '',
        'sort'        => '',
        'filters'     => '',
        'max-results' => '',
    ],
];
Array
(
    [0] => Array
        (
            [0] => 929
        )
)

# 今日、昨日、一昨日のセッション数
$query = [
    'startdate' => '2daysAgo',
    'enddate'   => 'today',
    'metrics'   => 'ga:sessions',
    'options' => [
        'dimensions'  => 'ga:date',
        'sort'        => '-ga:date',
        'filters'     => '',
        'max-results' => '',
    ],
];
Array
(
    [0] => Array
        (
            [0] => 20160901
            [1] => 6
        )
    [1] => Array
        (
            [0] => 20160831
            [1] => 28
        )
    [2] => Array
        (
            [0] => 20160830
            [1] => 24
        )
)

# セッション推移 年区切り、月区切り、日区切り
$query = [
    'startdate' => '2016-08-01',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:sessions',
    'options' => [
        'dimensions'  => 'ga:year',
        'sort'        => '-ga:year',
        'filters'     => '',
        'max-results' => '',
    ],
];
Array
(
    [0] => Array
        (
            [0] => 2016
            [1] => 929
        )
)
$query = [
    'startdate' => '2016-08-01',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:sessions',
    'options' => [
        'dimensions'  => 'ga:yearMonth',
        'sort'        => '-ga:yearMonth',
        'filters'     => '',
        'max-results' => '',
    ],
];
Array
(
    [0] => Array
        (
            [0] => 201609
            [1] => 6
        )
    [1] => Array
        (
            [0] => 201608
            [1] => 923
        )
)
$query = [
    'startdate' => '2016-08-29',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:sessions',
    'options' => [
        'dimensions'  => 'ga:date',
        'sort'        => '-ga:date',
        'filters'     => '',
        'max-results' => '',
    ],
];
Array
(
    [0] => Array
        (
            [0] => 20160901
            [1] => 6
        )
    [1] => Array
        (
            [0] => 20160831
            [1] => 28
        )
    [2] => Array
        (
            [0] => 20160830
            [1] => 24
        )
    [3] => Array
        (
            [0] => 20160829
            [1] => 35
        )
)

# デバイス 区切りはなしで、期間のみ
$query = [
    'startdate' => '2016-07-01',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:sessions',
    'options' => [
        'dimensions'  => 'ga:deviceCategory',
        'sort'        => '',
        'filters'     => 'ga:deviceCategory==desktop,ga:deviceCategory==mobile,ga:deviceCategory==tablet',
        'max-results' => '',
    ],
];
Array
(
    [0] => Array
        (
            [0] => desktop
            [1] => 1799
        )
    [1] => Array
        (
            [0] => mobile
            [1] => 30
        )
    [2] => Array
        (
            [0] => tablet
            [1] => 67
        )
)

# ページごとページ別のアクセス
$query = [
    'startdate' => '2016-07-01',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:pageviews',
    'options' => [
        'dimensions'  => 'ga:pagePath,ga:pageTitle',
        'sort'        => '-ga:pageviews',
        'filters'     => 'ga:pagePath!@share',
        'max-results' => '3',
    ],
];
Array
(
    [0] => Array
        (
            [0] => /
            [1] => SITE
            [2] => 267
        )
    [1] => Array
        (
            [0] => /?eid=694
            [1] => フリーゲーム「OFF」 | SITE
            [2] => 157
        )
    [2] => Array
        (
            [0] => /?eid=600
            [1] => Skyblockをマルチで | SITE
            [2] => 153
        )
)

# 検索キーワード notprovidedを抜いた版
$query = [
    'startdate' => '2016-07-01',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:organicSearches',
    'options' => [
        'dimensions'  => 'ga:pagePath,ga:pageTitle,ga:keyword',
        'sort'        => '-ga:organicSearches',
        'filters'     => 'ga:keyword!@not set;ga:keyword!@not provided;ga:keyword!@share;ga:keyword!@cookie',
        'max-results' => '3',
    ],
];
Array
(
    [0] => Array
        (
            [0] => /?eid=694
            [1] => フリーゲーム「OFF」 | SITE
            [2] => off ゲーム ネタバレ
            [3] => 7
        )
    [1] => Array
        (
            [0] => /?eid=694
            [1] => フリーゲーム「OFF」 | SITE
            [2] => off ネタバレ
            [3] => 5
        )
    [2] => Array
        (
            [0] => /?eid=302
            [1] => 王政錬金術師のなり方 | SITE
            [2] => マビノギ 王政錬金術師
            [3] => 3
        )
)

# 検索キーワード notprovidedも含める
$query = [
    'startdate' => '2016-07-01',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:organicSearches',
    'options' => [
        'dimensions'  => 'ga:pagePath,ga:pageTitle,ga:keyword',
        'sort'        => '-ga:organicSearches',
        'filters'     => 'ga:keyword!@not set;ga:keyword!@share;ga:keyword!@cookie',
        'max-results' => '3',
    ],
];
Array
(
    [0] => Array
        (
            [0] => /?eid=694
            [1] => フリーゲーム「OFF」 | SITE
            [2] => (not provided)
            [3] => 92
        )
    [1] => Array
        (
            [0] => /?eid=600
            [1] => Skyblockをマルチで | SITE
            [2] => (not provided)
            [3] => 85
        )
    [2] => Array
        (
            [0] => /?eid=760
            [1] => Python python3でウェブサーバを作る | SITE
            [2] => (not provided)
            [3] => 66
        )
)

# 絞り込みについて
$query = [
    'startdate' => '2016-07-01',
    'enddate'   => '2016-09-01',
    'metrics'   => 'ga:pageviews',
    'options' => [
        'dimensions'  => 'ga:pagePath,ga:pageTitle',
        'sort'        => '-ga:pageviews',
        # 演算子の意味 ==(一致) !=(一致しない) =@(含む) !@(含まない)
        # ;をつけると「かつ」になる
        # ,をつけると条件ごとにわける
        # 一番最後に;つけたくなるけどつけないこと
        'filters'     => 'ga:pagePath=@aaaaaaaaaa,ga:pagePath=@bbbbbbbbbb',
        'max-results' => '3',
    ],
];
# 条件は違うけどこんなふうに出るよ
array(2) {
  [0]=>
  array(3) {
    [0]=>
    string(37) "/facility/a/"
    [1]=>
    string(100) "保育園"
    [2]=>
    string(4) "1149"
  }
  [1]=>
  array(3) {
    [0]=>
    string(26) "/facility/b/"
    [1]=>
    string(53) "保育園"
    [2]=>
    string(3) "875"
  }
}

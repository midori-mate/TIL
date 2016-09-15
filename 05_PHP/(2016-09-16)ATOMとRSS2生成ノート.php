<?php

/*
ATOMとRSS2.0の生成ノート。
*/

# このヘッダのあとにxml形式のテンプレートを出力すればよい。
header('Content-type:text/xml; charset=UTF-8');

# 日付はxml用の形式にしないといけない。
$timestamp = strtotime($data['2016/01/01']);
$date4xml = date('D, d M Y h:i:s O', $timestamp);

# ATOMの
$atom = <<<EOF
<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xml:lang='ja'>
    <id>{サイトのURLでもいれときゃいいんじゃない}</id>
    <title>{フィードのタイトル}</title>
    <updated>{最終更新日}</updated>
    <link rel='alternate' type='text/html' href='{サイトのURL}' />
    <link rel='self' type='application/atom+xml' href='{フィードのURL}' />
{foreach $recordData as $data}
    <entry>
        <id>{シングルページのURLでもいれときゃいいんじゃない}/</id>
        <title>{シングルページのタイトル}</title>
        <link rel='alternate' type='text/html' href='{シングルページのURL}' />
        <updated>{更新日}</updated>
        <summary>{内容}</summary>
    </entry>
{/foreach}
</feed>
EOF;

# RSS2.0の
$rss2 = <<<EOF
<?xml version='1.0' encoding='UTF-8'?>
<rss version='2.0'>
    <channel>
        <title>{フィードのタイトル}</title>
        <link>{サイトのURL}</link>
        <description>{サイトの説明}</description>
{foreach $recordData as $data}
        <item>
            <title>{シングルページのタイトル}</title>
            <link>{シングルページのURL}</link>
            <description>{内容}</description>
            <pubDate>{更新日}</pubDate>
        </item>
{/foreach}
    </channel>
</rss>
EOF;




<?php

# atom
$url1 = "http://qiita.com/mpyw/feed.atom";
$atom = simplexml_load_file($url1);
print_r($atom->getNamespaces());
/*[
    [] => http://www.w3.org/2005/Atom
    [xml] => http://www.w3.org/XML/1998/namespace
]*/

# rss1?
$url2 = "http://guild-elf.jugem.jp/?mode=rss";
$rss = simplexml_load_file($url2);
print_r($rss->getNamespaces());
/*[
    [rdf] => http://www.w3.org/1999/02/22-rdf-syntax-ns#
    [xml] => http://www.w3.org/XML/1998/namespace
]*/

$url3 = "http://higesusk.blog.fc2.com/?xml";
$RSS = simplexml_load_file($url3);
print_r($RSS->getNamespaces());
/*[
    [rdf] => http://www.w3.org/1999/02/22-rdf-syntax-ns#
    [xml] => http://www.w3.org/XML/1998/namespace
]*/



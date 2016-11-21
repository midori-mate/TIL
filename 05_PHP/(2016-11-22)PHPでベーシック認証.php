<?php

switch (true) {
    case !isset($_SERVER['PHP_AUTH_USER'], $_SERVER['PHP_AUTH_PW']):
    case $_SERVER['PHP_AUTH_USER'] !== 'user':
    case $_SERVER['PHP_AUTH_PW'] !== 'pass':
        header('WWW-Authenticate: Basic realm="Enter username and password."');
        header('Content-Type: text/plain; charset=utf-8');
        die('このページを見るにはログインが必要です');
}

header('Content-Type: text/html; charset=utf-8');
echo 'ログイン成功<br>';

print('<pre>');print_r($_SERVER);print('</pre>');exit();


<?php

# ==============================
# ローカルxampp環境
#     C:/xampp/sendmail/sendmail.ini
#         サーバ名をmail.domain.co.jp(一例)
#         ポートを587
#         あとauth_username,auth_password,force_senderとかをてきとーなメアド、パスで埋める
#     php.ini
#         sendmail_path = "\"C:\xampp\sendmail\sendmail.exe\" -t" 有効化
#         これのちょっと下に同じ変数があるから、そっちはコメントアウトする。上書きされちゃうからね。
#     そんでxamppリセット
# ==============================

# ==============================
# centos環境
#     sendmailが使えるか確認
#         echo "example!!" | /usr/sbin/sendmail -t -i "username@domain.co.jp"; コンソールで実行
#     SELinuxを無効化する
#         コンソールで getenforce 結果がEnforcingだったら setenforce 0 でPermissiveにする
# ==============================

# ==============================
# MAC環境
#     php.ini
#         sendmail_path は /usr/sbin/sendmail -t -i
#
#     /etc/postfix/domain_passwd を作る。
#         mail.domain.co.jp:587 username@domain.co.jp:password
#
#     /etc/postfix
#         パーミッション開放
#
#     $ sudo postmap domain_passwd
#         domain_passwd.dbができる。_passwdは消していい。
#
#     /etc/postfix/main.cf追記
#         relayhost = mail.domain.co.jp:587
#         smtp_sasl_auth_enable = yes
#         smtp_sasl_password_maps = hash:/etc/postfix/domain_passwd
#         smtp_sasl_security_options = noanonymous
#         smtp_use_tls = yes
#         smtp_tls_security_level = encrypt
#         tls_random_source = dev:/dev/urandom
#
#     そして、メール送るときはreturn pathをつけましょう。
#
# 以上の処置で解決したときの状況を以下に。
#     ● yahooのアドレスには届く
#     ● domain宛に届かない
#     ● 送信失敗したメールが /var/spool/postfix/deferred に溜まってる
#     ● $ mailq のログに、hostがお前のメールを拒否してるって書いてある
# ==============================
# また別のときの状況。
#     ● $ mailq のログに TLS is required, but our TLS engine is unavailable って出てた。
#     main.cf にこれを書いたらそのエラーは出なくなった。意味はしらん。
#         smtp_tls_CAfile = /etc/pki/tls/cert.pem
#         smtp_tls_security_level = may
#         smtp_tls_loglevel = 1
#
# mailqの削除
#     # sudo postsuper -d ALL
# ==============================
# さらに別の状況
#     ● メールを送ると You have new mail in /var/mail/username と出るけどThunderbirdには届かない……

# 送信コード
$to                 = 'user@yahoo.co.jp';
$subject            = 'アルプスの殺人少女';
$message            = '先天的殺人鬼や!';
$additional_headers = 'From: username@domain.co.jp';
$additional_param   = '-f username@domain.co.jp';
$result = mb_send_mail($to, $subject, $message, $additional_headers, $additional_param);

# ここでtrueが出ても、ただコマンドが無事終了したって意味だからあんま意味ない。
var_dump($result);
# 書きのがしてることあるかもしれないから
# うまくいかんなら清凉会メモをご覧あれ

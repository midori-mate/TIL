
SQLserverNote (検索用 SQL Server)
===

## 環境作成

- SSMS と SQLserver インストール。
- SSMSで自分のPC名を選択してWindows認証。

## 場合別tips

### 01. 認証が2種類あんの何?

- Windows認証: デフォルトの認証。
- SQL Server認証: 専用ユーザ、パスワードでの認証。

### 02. セキュリティ > ログイン にある sa って何?

最高権限をもつユーザ。Mysqlのrootみたいなもんかな? sysadminロールを持つ。

ただし使用は推奨されないっていうかMicrosoftはSQL Server認証自体を認証してない。デフォルトでは無効になっている。(アイコンにバツがついてる。)

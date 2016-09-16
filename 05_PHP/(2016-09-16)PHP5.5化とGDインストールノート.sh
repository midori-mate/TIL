
# 状況としては、PHP5.3がサーバのメインPHPとしてインストールされている状態。

# GDライブラリの追加。
yum install php-gd

# epelのリポジトリ追加。
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

# remiのリポジトリ追加。
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm

# 5.5インストールに必要なパッケージを追加。
yum install libxslt t1lib libXpm

# 標準のリポジトリを一時的に切る。viはむずかしーので直接やる。
# 全項目に enabled=0 を追加。
vi /etc/yum.repos.d/CentOS-Base.repo

# インストール。
yum install --enablerepo=remi,remi-php55 php php-devel php-mbstring php-mcrypt php-mysqlnd php-fpm php-pear php-opcache php-gd

# バージョン確認。5.5.32が出た。完了。
php -v



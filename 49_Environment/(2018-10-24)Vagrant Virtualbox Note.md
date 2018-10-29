Vagrant Virtualbox Note
===

## インストール

とにかくこいつらをインストール。まずこれ。

[Vagrant](https://www.vagrantup.com/)

[Virtualbox](https://www.virtualbox.org/)

## イチから始める(Vagrantfileがない)場合

### 01. ひとつディレクトリを用意する。

そこにVMを作ることになる。

### 02. init

そのディレクトリでコマンドライン開いて……

```bash
$ vagrant init
```

ディレクトリに Vagrantfile ができる。

### 03. どのOSにする?

[Vagrantbox.es](https://www.vagrantbox.es/)

この中から欲しい感じのboxファイルを探してURLをコピー。そしてVagrantfileに以下のように書く。すでにvm.boxのほうはあるるのでそこんとこに。

```ruby
config.vm.box = "[ここに作るVMの名前]"
config.vm.box_url = "[ここに上でコピーしたURL]"

# 例
config.vm.box = "CentOS7.2"
config.vm.box_url = "https://github.com/CommanderK5/packer-centos-template/releases/download/0.7.2/vagrant-centos-7.2.box"
```

### 04. VMを作る

上のboxファイルをDLするからちょっと__時間かかる。__

```bash
$ vagrant up
```

### 05. ネットワーク設定

Vagrantfile

```ruby
config.vm.network "private_network", ip: "192.168.33.10"
```

最初から書いてあるからコメントアウトするだけ。これやるとFTPでアクセスできる。あとでapacheにアクセスするときも要るし。

### 06. フォルダ同期

Vagrantfile

```ruby
config.vm.synced_folder "ホストPC側のパス", "Vagrant側のパス"

# 例 相対パスにしとくとVagrantfileを人に渡すときラクだって
config.vm.synced_folder ".", "/var/www/html"
```

これも最初から書いてある。これができるっていうのがVagrantに手を出した一番の理由。

### 07. さて試しにPHPを入れてみようか

```bash
# まずVMにログイン
$ vagrant ssh

# rootになろう パスワードは vagrant
$ su -

# apache入れる
$ yum -y install httpd

# もともとのPHP消す
$ yum remove php-*

# PHP入れる
$ rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
$ yum install --enablerepo=remi,remi-php70 php php-devel php-mbstring php-pdo php-gd php-xml php-mcrypt

# 入ったか確認したいよね
$ httpd -v
$ php -v
```

- Vagrantfile のあるフォルダに phpinfo.php だの index.php だの置いて。
- `http://192.168.33.10/phpinfo.php` とかでアクセス。

### 08. さて試しにPythonを入れてみようか

```bash
$ yum install -y https://centos7.iuscommunity.org/ius-release.rpm
$ yum install python36u python36u-libs python36u-devel python36u-pip
$ python3.6 -V
```

- Vagrantfile のあるフォルダにてきとうにpyファイル置いて。
- `$ python3.6 /var/www/html/py.py`

## Vagrant コマンド

### 基本

```bash
# 起動
$ vagrant up

# 状態確認
$ vagrant status

# VM停止
$ vagrant halt

# 再起動
$ vagrant reload

# ログイン
$ vagrant ssh

# ローカルにbox追加
$ vagrant box add [名前] [URL]
# 例
$ vagrant box add CentOS7.2 https://github.com/CommanderK5/packer-centos-template/releases/download/0.7.2/vagrant-centos-7.2.box

# box削除
$ vagrant box remove [名前]

# 追加済みのbox一覧
$ vagrant box list

# 存在してるboxを書き出す(haltしたあとに行う)
$ vagrant package
```

### CentOSの中にいるとき

```bash
# 出る
$ exit
```




## 参考サイト

[MacにVagrantでCentOS7環境を作成](https://qiita.com/sudachi808/items/3614fd90f9025973de4b)

[VagrantコマンドとVagrantfileの設定メモ](https://qiita.com/TsukasaGR/items/2d47eae4d8f9c0fe5cd5)


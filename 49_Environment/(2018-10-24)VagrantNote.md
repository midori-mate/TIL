Vagrant Note
===



## インストール

とりあえずこれインストール。とにかくこれ。

- [Vagrant](https://www.vagrantup.com/)
- [Virtualbox](https://www.virtualbox.org/)

## イチから始める場合

Vagrantfileがあるなら `$ vagrant up` だけやりゃいいです。

1. ひとつディレクトリを用意。
2. ディレクトリでコンソール開く。
    - `$ vagrant init`
    - Vagrantfile ができる。
3. Vagrantfile 中身を埋める。とりあえずこのへんを書いとこう。
    - 欲しい感じのOSをここ( [Vagrantbox.es](https://www.vagrantbox.es/) )から探してURLをコピー。
        - `config.vm.box = "[ここに作るVMの名前 CentOS7.2とか]"`
        - `config.vm.box_url = "[ここに上でコピーしたURL]"`
    - ローカルIPを設定。
        - `config.vm.network "private_network", ip: "192.168.33.10"`
    - フォルダ同期。相対パスを書いとくといい。
        - `config.vm.synced_folder ".", "/var/www/html"`
    - provision(VM作成後にVM内で実行するコマンド)設定。
        - `config.vm.provision :shell, :path => "provision/provision.sh"`
        - Vagrantfile の隣に `provision/provision.sh` ファイル作成。
4. VM作成!
    - `$ vagrant up`

まあこれで完成はしてんだけど……いろいろいじる方法は以下。

- `$ vagrant ssh` でVMの中にのコンソールに入れる。ユーザーは root じゃなくて vagrant 。
- `$ su -` で管理者権限になれる。パスワードは vagrant 。
- `$ exit` VMの中でこう打つとVMから出れる。
- `$ vagrant halt` でVMをシャットダウン。
- FTPアプリで中を見るときは `192.168.33.10` でユーザは `vagrant:vagrant` 。

他の便利コマンドはさらに以下。

## Vagrant コマンド

```bash
# ともかくぱそこ内全部のVMの状態を見たい。
$ vagrant global-status

# 停止したい。
$ vagrant halt

# つーかむしろ消したい。
$ vagrant destroy

# 起動したい。
$ vagrant up

# Vagrantfile を書き直したから再起動したい。
$ vagrant reload

# provision だけやり直したい。
$ vagrant provision
```

## PHP が欲しいときの provision.sh

```bash
#!/bin/sh

echo '----- Install apache -----'
yum -y install httpd

echo '----- Install remove default PHP -----'
yum remove php-*

echo '----- Install PHP7.0 -----'
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
yum install --enablerepo=remi,remi-php70 php php-devel php-mbstring php-pdo php-gd php-xml php-mcrypt
```

- 入ったか確認したいよね
    - `$ httpd -v`
    - `$ php -v`

## Python が欲しいときの provision.sh

```bash
#!/bin/sh

echo '----- Install ius-release.rpm -----'
yum install -y https://centos7.iuscommunity.org/ius-release.rpm

echo '----- Install Python3.6 -----'
yum install -y python36u python36u-libs python36u-devel python36u-pip

echo '----- Install pip for Python3.6 -----'
python3.6 -m ensurepip

echo '----- Update pip -----'
python3.6 -m ensurepip --upgrade
```

pip を普通に書いてないのは、なんか pip ってやるとデフォルトで入ってる 2.7 のほうに紐付いちゃう感じなんだよねーよくわかんない。

- 確認。
    - `$ python3.6 -V`

## Python Django が欲しいとき

Vagrantfile に forwarded_port 追加。ホストマシンポート12345へのアクセスをゲストマシンポート8000へ自動で流す。

```ruby
config.vm.network "forwarded_port", guest: 8000, host: 12345
```

provision.sh は上述の Python 用に加えてこれを。

```bash
echo '----- Install django module -----'
python3.6 -m pip install django
```

Django を起動するときはこれで。

```bash
$ python3.6 /vagrant/app/manage.py runserver 0.0.0.0:8000
```

## ポートがあいてんのか確かめる

Vagrantfile で指定したポートがあいてないとVMが起動しないから、目当てのポートを他プロセスが専有してねーかどうかチェックするときがたまにある。

ポートあいてんのか確認。(Mac)

```
Network Utility.app > Portsscan タブ > アドレスを 127.0.0.1 > ポートを限定してテスト
```

ポートを専有しているプロセスを確認。(Mac)

```
$ lsof -i:[PORT番号]
$ kill [上で出てきたプロセスのPID]
```
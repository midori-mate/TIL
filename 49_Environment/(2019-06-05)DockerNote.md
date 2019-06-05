DockerNote
===

## 所感

### 2019-06-05

pull,create,start の流れはとてもよくわかった。わからないのは以下。

- 「CentOS7 でかつ SFTP 接続できて Apache で配信できるのがほしーな」と思って調べてみると「centos7 Image」「sftp 用の Image」「ngix Image」など出てきて、「いやいや、どれかひとつかよ」ってなる。

この場合、 centos Image を最初に使って、他のプログラムをインストールしたあと Container から Image へコミットする感じになる??

- private_network が設定したいんだけどわからん。 Vagrant では以下のように設定できるやつ。

```ruby
config.vm.network "private_network", ip: "192.168.33.12"
```



## はじめて

### 基礎

- Docker Engine: Docker を使うための常駐プログラム
    - [https://hub.docker.com/editions/community/docker-ce-desktop-mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)

### Hub から Image 入手するばあい

```bash
# CentOS7 を入手してみようや
$ docker pull centos:centos7

# Image 一覧。
$ docker images

# Container 作成。
$ docker create --name foo -it centos:centos7 /bin/bash

# Container 一覧。
$ docker ps -a
# 実行しているものだけ。
$ docker ps

# Container 起動。
$ docker start foo

# 一時停止、再開、再起動、停止、削除
$ docker pause foo
$ docker unpause foo
$ docker restart foo
$ docker stop foo
$ docker rm foo

# Container の中に入る
$ docker exec -it foo /bin/bash

# これで start すれば最初から Container の中に入る
$ docker start -i foo
```

問題: `start` しても起動していない(ステータスが `Exited` になってる)
:   これは `create` のときに `-it centos:centos7 /bin/bash` をつけなかったとき発生した。
:   というより `Image Command` は最後につけるもの。


問題: `start` するときエラー `OCI runtime create failed: container_linux.go:344: starting container process caused "exec: \"-it\": executable file not found in $PATH": unknown.`
:   まあなんか `create` コマンドのオプション書く順番がおかしかったっぽい。

### Vagrant の forwarded_port は?

```ruby
config.vm.network "forwarded_port", guest: 80, host: 1991
```

```bash
# -p コマンド
$ docker create --name foo -p 80:1991 -it centos:centos7 /bin/bash
```

### Vagrant の private_network は?

問題: 要は cyberduck で接続したいんだけどその場合 atmoz/sftp っていう Image を使うことばっかり出てくる。え? CentOS7 でかつ sftp 接続したい、っていう発想はおかしいわけ??


## Vagrant の中で Docker を使うやつ

> [VagrantとDockerについて名前しか知らなかったので試した](https://qiita.com/hidekuro/items/fc12344d36d996198e96)

この記事は**ダメ**。 `run` のときに以下のようなコマンドがあるけど、これは動かない。

```bash
vagrant@vagrant-ubuntu-trusty-64:~$ docker run -i -t -v /vagrant:/tmp/shared --name="hogehoge" midori/my-bash
docker: Error response from daemon: OCI runtime create failed: container_linux.go:348: starting container process caused "process_linux.go:301: running exec setns process for init caused \"exit status 23\"": unknown.
```

これ(↓)なら動くけれど、結局その先の、 Vagrantfile に docker の起動を書くところでコケる。

```bash
# midori/my-bash Image から起動した foo Container で root ユーザで bash 起動
docker create --name foo -v /vagrant:/tmp/shared -it midori/my-bash /bin/bash
```

残念。でも Vagrant 内で全部完結というのはいいと思う。

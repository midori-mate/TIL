
Linux Command Note
===

## よく使うやつ

```bash
$ pwd
$ mount_smbfs '//user%20name%21%21:password@dir/free' '/Users/username/mount'
    # スペースは %20 ビックリマークは %21
$ tar cvzf ".tar.gz" ""
$ tar xvzf ".tar.gz"
$ mv "移動物" "移動先"
$ cp -p "index.php" ".ht--index.php@"
    # -pは全部の属性を引き継ぐ
$ su - username
    # ユーザ切り替え。書かなければルートになる。
$ less ""
$ cat ""
$ cp "original" "copy"
$ chmod 777 ""
$ chmod +x ""
$ rm ""
$ rm -rf "" (ディレクトリを再帰的に消す場合。rmは複数可能)
$ ln -s "ターゲット" "シンボ名"
$ wget -r -np {URL}
    # r = recursive, np = no parent
```

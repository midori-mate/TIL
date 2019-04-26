firewalldNote
===

MrrhpApache でさくらVPS(CentOS7)をいじってて、ファイアウォールのいじり方がわかったのでノートする。

## 基本

- 切っておけばアクセスし放題。
- 切ってる間はポートの開放設定は無効。

```bash
# 状態確認。
firewall-cmd --list-services --zone=public --permanent

# 起動、停止
systemctl start   firewalld
systemctl stop    firewalld
systemctl restart firewalld
```

## 各サービス用の開放

停止中はこれらを打っても無効。起動してから行うこと。

```bash
firewall-cmd --add-service=http  --zone=public --permanent
firewall-cmd --add-service=https --zone=public --permanent
firewall-cmd --add-service=mysql --zone=public --permanent
```

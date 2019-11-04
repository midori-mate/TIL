UbuntuNote
===

Ubuntu をちょっと触ってみたんでメモるよ。

## Vagrant で使う

Vagrantfile

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 80, host: 1984
  config.vm.network "private_network", ip: "192.168.33.12"
  config.vm.synced_folder ".", "/vagrant"
  # config.vm.provision :shell, :path => "vagrant-provision/provision.sh"
end
```

これで Ubuntu 16 が使える。

```plaintext
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-166-generic x86_64)
```

このあと Ubuntu 18 にするには `do-release-upgrade` する。

```bash
# -f 以降は y を押さなくていいように付けている。
do-release-upgrade -f DistUpgradeViewNonInteractive
lsb_release -a
# No LSB modules are available.
# Distributor ID: Ubuntu
# Description:    Ubuntu 18.04.3 LTS
# Release:        18.04
# Codename:       bionic
```

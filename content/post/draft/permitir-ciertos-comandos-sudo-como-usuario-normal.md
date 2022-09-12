---
title: Permitir ciertos comandos sudo como usuario normal
description: 
date: 2016-04-20
lastmod: 2016-04-20
slug: permitir-ciertos-comandos-sudo-como-usuario-normal
image: "covers/draft.png"
tags:
  - SUDO
categories:
  - Linux
---



```
llows members of the users group to mount and unmount the
## cdrom as root
%users  ALL=/sbin/mount /mnt/cdrom, /sbin/umount /mnt/cdrom
```

http://www.cyberciti.biz/tips/allow-a-normal-user-to-run-commands-as-root.html

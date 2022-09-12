---
title: Poner ip statica
description: 
date: 2015-11-10
lastmod: 2015-11-10
slug: ip_statica
image: "covers/linux.png"
tags:
  - ip
  - network
categories:
  - Linux
---


`vim /etc/network/interfaces`

```
auto eth0
inface eth0 inet static
address 192.168.1.3
netmask 255.255.255.0
gateway 192.168.1.1
```

`/etc/init.d/networking stop && /etc/init.d/networking start`

o

`/etc/init.d/networking restart`

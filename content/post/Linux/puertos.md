---
title: Ver puertos abiertos
description: 
date: 2015-10-03
lastmod: 2015-10-03
slug: puertos
image: "covers/linux.png"
tags:
  - nmap
  - ps
  - tcp
categories:
  - Linux
---



`sudo nmap -O localhost | grep "open"`

`sudo fuser -n tcp puerto`

`sudo ps -l PID`

`sudo /etc/init.d/aplicación stop`


###### matar por la fuerza

`sudo fuser -nk tcp puerto`

`sudo killall servicio`

`sudo kill -9 PID`

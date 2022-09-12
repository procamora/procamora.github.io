---
title: Crear chat con netcat
description: 
date: 2015-10-08
lastmod: 2015-10-08
slug: netcat
image: "covers/linux.png"
tags:
  - netcat
  - network
  - nc
categories:
  - Linux
---


## Para hacer un chat entre ordenadores en una red local

###### Servidor

`nc -l -p 6698`


###### Cliente

`nc ip-server 6698`


> Importante: La conversación se manda por paquetes tcp sin cifrar, por lo que con un sniffer(wireshark) en la red local se pueden leer los paquetes

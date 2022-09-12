---
title: Uso de dd
description: 
date: 2015-11-08
lastmod: 2015-11-08
slug: dd
image: "covers/linux.png"
tags:
  - dd
categories:
  - Linux
---


La orden **dd** hace una copia exacta byte a byte.

Ejemplos:

###### Clonar un disco duro:
`dd if=/dev/sda |pv|dd of=/dev/sdb`


######Clonar una partición:
`dd if=/dev/sdc2 |pv|dd of=/dev/sda1`


######Crear una imagen iso de una partición o disco duro (excelente opción para backups):
`dd if=/dev/sda1 |pv|dd of=/home/usuario/backup.iso`


> En algunas distros puede que pv no venga instalado, así que bastará con instalarlo para poder usar este tip.

---
title: Eliminar procesos por id
description: 
date: 2015-10-04
lastmod: 2015-10-04
slug: procesos
image: "covers/linux.png"
tags:
  - process
  - ps
  - kill
categories:
  - Linux
---


###### Mostrar procesos
`ps -A`


###### Matar proceso por pid
`sudo kill 'pid'`
> hay distintos números para mandar al proceso a la hora de matarlo 1..9


###### Matar procesos por nombre
`sudo killall php`


###### Matar por entorno gráfico
`sudo xkill`

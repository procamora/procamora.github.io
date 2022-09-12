---
title: Cascos bluetooth en Kali
description: 
date: 2016-02-23
lastmod: 2016-02-23
slug: cascos-bluetooth-en-kali
image: "covers/draft.png"
tags:
  - bluetooth
  - kali
categories:
  - Linux
---



## Primeros instalamos la librería para gestionar el bluetooth con pulseaudio

`sudo apt-get install pulseaudio-module-bluetooth` 

Iniciamos el servicio de bluetooth

`/etc/init.d/bluetooth start`


foto



Para poder activarlo en la configuración n hay que activar el modulo
`sudo pactl load-module module-bluetooth-discover`


después vamos a configuración de sonido y establecemos que el sonido salga por el casco en vez de por el altavoz

foto

---
title: Descargar video youtube con python
description: Cuando queremos descargar un video de youtube tenemos multiples opciones, tanto aplicaciones como online. La aplicacion que mejor resultados me ha dado es youtube-dl.
date: 2016-01-25
lastmod: 2016-01-25
slug: descargar-video-youtube-con-python
image: "covers/software.png"
tags:
  - python
  - youtube
  - pip
  - python
categories:
  - Software
---


# Introducción

Cuando queremos descargar un video de youtube tenemos multiples opciones, tanto aplicaciones como online. La aplicación que mejor resultados me ha dado es youtube-dl.



## youtube-dl

Permite tanto descargar videos como listas de reproducción.

`sudo pip install youtube-dl`


`$ youtube-dl -f "(bestvideo+bestaudio/best)" "https://www.youtube.com/watch?v=tbVmV4XJNlo"`

[Documentacion][doc]

[doc]: https://github.com/rg3/youtube-dl/blob/master/README.md#readme

## pytube

`sudo pip install pytube`

`pytube -e mp4 -r 720p "https://www.youtube.com/watch?v=tbVmV4XJNlo"`

[pytube]: https://github.com/nficano/pytube

Pd: No permite descargar vídeos a 1080 a fecha de hoy 22/01/2016



## pafy

Para instalar pafy

`sudo pip install pafy`

Download best available resolution (-b):

`$ ytdl -b "http://www.youtube.com/watch?v=cyMHZVT91Dw"`

para ver las calidades disponibles ejecutamos
ytdl tbVmV4XJNlo

y para seleccionar con que calidad queremos descargarnoslo:
ytdl -n2 cyMHZVT91Dw

Fuente: [pafy][pafy]

[pafy]: http://np1.github.io/pafy/

Pd: No permite descargar vídeos a 1080 a fecha de hoy 22/01/2016


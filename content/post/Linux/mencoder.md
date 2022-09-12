---
title: Cambiar formato videos
description: 
date: 2015-10-22
lastmod: 2015-10-22
slug: mencoder
image: "covers/linux.png"
tags:
  - mencoder
categories:
  - Linux
---


###### Cambiar formato de los vídeos
`mencoder -idx 'videooriginal.ogv' -ovc lavc -oac mp3lame -o 'videofinal.flv'`


###### Incluir subtítulos en un vídeo
`mencoder 'VideoOriginal.avi' -sub 'ArchivoDeSubtitulos.srt' -subcp utf-8 -oac copy -ovc xvid -xvidencopts pass=1 -o 'VideoDeSalida.avi'`


###### Unir 2 vídeos
`mencoder -oac copy -ovc copy -o 'video_completo.avi' 'parte1.avi' 'parte2.avi'`

---
title: Activar Tecla Suprimir
description: "Parece ser que la combinación en las versiones de GNOME Shell a utilizar son: CTRL + supr si quieres que pasen por la papelera o SHIFT + supr si quieres eliminar archivos o carpetas directamente."
date: 2015-12-27
lastmod: 2015-12-27
slug: activarteclasuprimir
image: "covers/linux.png"
tags:
  - linux
  - gnome shell
categories:
  - Linux
---



Parece ser que la combinación en las versiones de GNOME Shell a utilizar son: CTRL + supr si quieres que pasen por la papelera o SHIFT + supr si quieres eliminar archivos o carpetas directamente.

En las ediciones modernas de este escritorio (GNOME Shell 3.6 para arriba) una forma sencilla de hacerlo es siguiendo el método que nos proponen en la wiki de Arch que consiste en editar el archivo oculto de nuestro directorio personal `~/.config/nautilus/accels` (una copia de seguridad del archivo antes de tocarlo nunca de está de más..)

Se trata de modificar la linea:
1
	
`; (gtk_accel_path "<Actions>/DirViewActions/Trash" "<Primary>Delete")`

descomentándola quitándole el punto y coma (;) del principio de la linea y eliminando donde pone <Primary>, tal que como figura en la captura de imagen:
1
	
`(gtk_accel_path "<Actions>/DirViewActions/Trash" "Delete")`

Después tan solo tenemos que guardar los cambios, reiniciar nautilus y ya dispondremos de nuestra tecla de suprimir activada :-)

Hay que decir que este cambio no deshabilita ninguno de los atajos de teclado que tengáis establecidos previamente.


Fuentes: [1][0]
[0]: http://lamiradadelreplicante.com/2014/11/17/activar-la-tecla-suprimir-en-gnome-shell/

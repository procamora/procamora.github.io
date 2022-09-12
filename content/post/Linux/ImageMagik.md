---
title: Modificar imágenes con ImageMagik
description: 
date: 2015-11-11
lastmod: 2015-11-11
slug: ImageMagik
image: "covers/linux.png"
tags:
  - imagemagik
  - console
  - iamge
categories:
  - Linux
---


El comando convert nos permite realizar distintos tipos de conversiones en una imagen. La opción -resize sirve cambiar el tamaño. Veamos unos ejemplo sencillos:

`sudo convert elefante.jpg elefante.png`
`sudo convert elefante.jpg -resize 640×480 elefantemini.jpg`
`sudo convert elefante.jpg -resize 640×480 elefante.png`

En el primer ejemplo hemos cambiado de formato, en el segundo de tamaño y en el tercero de formato y tamaño a la vez.


##Reducir imágenes

######Tenemos varias imágenes. Podemos escribir uno a uno los nombres de cada imagen, pero si son muchas resultaría demasiado lento. Lo mejor es meterlas todas en una misma carpeta. Luego abrimos una terminal, dentro de la carpeta, y escribimos:

`sudo convert "*.jpg" -resize 150×150 imagen%02d.png`

>Con "*.jpg" le estamos diciendo al programa que tome como entrada a todos los archivos que terminen en .jpg que hay en ese directorio; con imagen%02d.png estamos diciendo que los archivos de salida serán en formato png y su nombre estará formado por la palabra imagen seguida de un número formado por dos dígitos (imagen00, imagen01, imagen02, imagen03,…); si tenemos más de 100 y necesitamos usar 3 dígitos escribiremos %03d, en lugar de %02d.

Aunque le hayamos dicho que las reduzca todas a una tamaño de 150×150 pixeles, convert respetara siempre las proporciones de la imagen original (asignando los 150 pixeles a uno solo de los lados). Si queremos que la anchura sea siempre la misma, y sea la altura lo que varíe, escribiremos solo el primero de los valores (-resize 150). Si, por el contrario, queremos que sea la altura lo que permanezca constante, escribiremos el segundo valor precedido del signo x  (-resize x150). Y si lo que queremos es que se ajuste al ancho y alto que hemos determinado, ignorando las proporciones de la imagen original, añadiremos \! (barra invertida exclamación); ejemplo:  -resize 150×150\!, cuando las proporciones no coincidan la imagen se deformará para ajustarse al tamaño asignado.

######Si tenemos muchas imágenes puede ser más rápido si escribimos:

`sudo convert "*.jpg"[150x150] imagen%02d.png`

Esto hará que, en lugar de leer primero todas las imágenes y luego reducirlas, las vaya reduciendo según las va leyendo; con esto el ordenador irá más rápido y consumirá menos recursos.

Podemos, también, reducir las imágenes en un tanto por ciento, por ejemplo escribiendo -resize 50% las reduciremos a la mitad.

Ahora vamos a ver otras opciones para reducir imágenes:

thumbnail

######Esta opción esta pensada para reducir el tamaño de imágenes muy muy grandes. Combina tres opciones: -strip elimina la información adicional que suele acompañar a las fotos de las cámaras digitales y a las imágenes tratadas con algunos programas de retoque fotográfico; -sample reduce varias veces la imagen; y -resize da el tamaño final. Por ejemplo:

`sudo convert "*.jpg" -thumbnail 150×150 imagen%02d.png

scale

######Es una versión simplificada de resize. Es más rápido y ligero, pero la imagen resultante puede perder algo de calidad.

`convert "*.jpg" -scale 150×150 imagen%02d.png`

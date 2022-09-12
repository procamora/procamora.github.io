---
title: Uso de estenagrofia
description: 
date: 2015-09-12
lastmod: 2015-09-12
slug: estenagrogafia_windows
image: "covers/windows.png"
tags:
  - windows
  - estenagrogafia
categories:
  - Windows
---


`copy /B archivo1+archivo2+archivoN archivoNuevo`


Pasos:
===========================

1) el gringo creo la carpeta "X" en el disco duro C: (esto para hacer el proceso mas fácil)

2) Seguidamente copio a esa carpeta, los archivos que realmente desea compartir y también la imagen que servirá solo como fachada

3) Seleccionas los "archivos importantes" y los comprimes dentro de un archivo con un nombre corto (para facilitar el tramite) el gringo le dio el nombre "X", pero pudo haberle puesto "PERRO", "GATO", etc.
Realmente puede usar cualquier compresor sea Winrar o Winzip para crear el comprimido.
4) Te vas a usar la linea de comandos para eso pulsas: INICIO > EJECUTAR o START > RUN en ingles.
Seguidamente escribe CMD y pulsas ENTER.
A continuación estarás en una ventana de fondo negro en donde:
A) escribirás: `CD\X` y pulsa ENTER (entrar a la carpeta que contiene los archivos)
B) escribes COPY /B [nombre de archivo de imagen.extensión] + [nombre de archivo comprimido.extensión] [Nombre del archivo destino.extensión JPG]

Segun el video:
`COPY /B cow.jpg + x.7z secretcow.jpg`

y Listo!!!
al abrir el archivo secretcow.jpg normalmente lo que encuentra en primer lugar es la cabecera del archivo de imagen y abre la imagen.

Pero si abres 7zip Manager (7zip si es obligatorio para sacar los archivos ocultos) podrás abrir el archivo SECRETCOW.jpg y lo que te aparecerán son los archivos contenidos dentro del archivo comprimido.

Los descomprimes y listo.

>Nota: No solamente funciona con JPG sino tambien con archivos GIF (ya lo probé) y tal vez funcione con otros tipos de archivos.

---
title: Restaurar disco con Clonezilla
description: En este ejemplo queremos restaurar la imagen del disco  **sda**  que esta guardada en el disco **sdb**
date: 2018-02-16
lastmod: 2018-02-16
slug: restaurar-disco-con-clonezilla
image: "covers/software.png"
tags:
  - clonezilla
  - linux
  - backup
categories:
  - Software
---



# Introducción:


- [Configuración Inicial](#header0)
- [Restauración del Disco](#header1)




En este ejemplo queremos restaurar la imagen del disco  **sda**  que esta guardada en el disco **sdb**.


# Configuración Inicial {#header0}



Lo primero es seleccionar el idioma y el teclado, una vez hecho eso podemos iniciar Clonezilla de modo gráfico o en modo consola para introducir el comando a ejecutar directamente. En este caso lo haremos de forma gráfica con **Start_Clonezilla**.

![1][Restaurar1]





En la mayoría de las ocasiones usaremos la opción **device-image**, ya que queremos restaurar una imagen de un directorio a un disco.

![1][Restaurar2]





Seleccionamos el modo de conectarnos con el disco en el tenemos la imagen que queremos restaurar, en nuestro caso sera **local_dev** que es un disco local.


![1][Restaurar3]





Ahora tenemos que conectar el disco al equipo en caso de que no estuviese conectado, pulsamos **Enter** para que escanee los discos disponibles.

![1][Restaurar4]





Aquí veremos los discos que hay disponibles, tenemos:

- **sda**: disco en el que queremos restaurar la imagen
- **sdb**: disco donde tenemos la imagen del disco sda

![1][Restaurar5]





Aquí vemos todas las particiones disponibles, tenemos que seleccionar el disco donde tenemos la imagen que queremos restaurar, ya que se va a montar para poder acceder a los directorios, en este caso **sdb1**.

![1][Restaurar6]





Seleccionamos el directorio donde esta la imagen a restaurar, en este caso la raíz y le damos a **Done**. Nos pedirá que le demos a **Enter** para confirmar.


![1][Restaurar9]





# Restauración del Disco {#header1}





Seleccionamos **restoredisk** ya que lo que deseamos hacer es restaurar una imagen.

![1][Restaurar10]





Nos saldrá la lista de imágenes disponibles para restaurar en el directorio que indicamos anteriormente, en esta ocasión solo tenemos 1 disponible por lo que la seleccionamos.


![1][Restaurar11]





Seleccionamos cual es el disco que queremos restaurar, aquí nunca saldrá el disco que hemos montado anteriormente para guardar la copia, en este caso el disco que queremos restaurar es **sda**.

![1][Restaurar12]






Aquí nos empezara a pedir unas configuraciones básicas, mi recomendación es dejarlas todas por defecto, la opción por defecto es **Yes, check the image before restoring** para chekear la integridad de la imagen antes de restaurarla.

![1][Restaurar13]





Indicamos que cuando termine se apague con **poweroff**, ya que es un proceso largo y posiblemente no estemos cuando termine de clonarse.

![1][Restaurar14]





Nos muestra el comando que se va a ejecutar por si queremos usarlo la próxima vez automatizando todo el proceso y nos pide que pulsemos **Enter** para confirmar la operación.

![1][Restaurar15]





Hace el checkeo de la imagen si anteriormente así lo indicamos como viene por defecto.

![1][Restaurar16]





Nos muestra lo que se va a hacer y nos pide confirmación 2 veces.

![1][Restaurar17]





Empieza el proceso de clonado de cada partición de **sda** en una carpeta de **sdb**.

![1][Restaurar18]



[Restaurar1]: /images/2018/ClonezillaRestaurar/1_ClonezillaRestaurar.png
[Restaurar2]: /images/2018/ClonezillaRestaurar/2_ClonezillaRestaurar.png
[Restaurar3]: /images/2018/ClonezillaRestaurar/3_ClonezillaRestaurar.png
[Restaurar4]: /images/2018/ClonezillaRestaurar/4_ClonezillaRestaurar.png
[Restaurar5]: /images/2018/ClonezillaRestaurar/5_ClonezillaRestaurar.png
[Restaurar6]: /images/2018/ClonezillaRestaurar/6_ClonezillaRestaurar.png
[Restaurar9]: /images/2018/ClonezillaRestaurar/9_ClonezillaRestaurar.png
[Restaurar10]: /images/2018/ClonezillaRestaurar/10_ClonezillaRestaurar.png
[Restaurar11]: /images/2018/ClonezillaRestaurar/11_ClonezillaRestaurar.png
[Restaurar12]: /images/2018/ClonezillaRestaurar/12_ClonezillaRestaurar.png
[Restaurar13]: /images/2018/ClonezillaRestaurar/13_ClonezillaRestaurar.png
[Restaurar14]: /images/2018/ClonezillaRestaurar/14_ClonezillaRestaurar.png
[Restaurar15]: /images/2018/ClonezillaRestaurar/15_ClonezillaRestaurar.png
[Restaurar16]: /images/2018/ClonezillaRestaurar/16_ClonezillaRestaurar.png
[Restaurar17]: /images/2018/ClonezillaRestaurar/17_ClonezillaRestaurar.png
[Restaurar18]: /images/2018/ClonezillaRestaurar/18_ClonezillaRestaurar.png


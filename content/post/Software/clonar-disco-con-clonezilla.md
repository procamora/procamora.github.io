---
title: Clonar disco con Clonezilla
description: En este ejemplo queremos hacer una copia del disco **sda** en el directorio raíz del disco **sdb**
date: 2018-02-16
lastmod: 2018-02-16
slug: clonar-disco-con-clonezilla
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
- [Clonación del Disco](#header1)




En este ejemplo queremos hacer una copia del disco **sda** en el directorio raíz del disco **sdb**.




# Configuración Inicial {#header0}



Lo primero es seleccionar el idioma y el teclado, una vez hecho eso podemos iniciar Clonezilla de modo gráfico o en modo consola para introducir el comando a ejecutar directamente. En este caso lo haremos de forma gráfica con **Start_Clonezilla**.

![1][Clonar1]





En la mayoría de las ocasiones usaremos la opción **device-image**, ya que queremos crear una copia del disco físico en un directorio de otro disco

![1][Clonar2]





Seleccionamos el modo de conectarnos con el disco en el que guardaremos la copia, en nuestro caso sera **local_dev** que es un disco local.

![1][Clonar4]





Ahora tenemos que conectar el disco al equipo en caso de que no estuviese conectado, pulsamos **Enter** para que escanee los discos disponibles.

![1][Clonar5]





Aquí veremos los discos que hay disponibles, tenemos:

- **sda**: disco del que queremos hacer una clonación
- **sdb**: disco donde guardaremos el disco sda


![1][Clonar6]





Aquí vemos todas las particiones disponibles, tenemos que seleccionar el disco donde queremos que se guarde la copia, ya que se va a montar para poder acceder a los directorios, en este caso **sdb1**.


![1][Clonar7]





Seleccionamos el directorio donde queremos que se guarde la copia, en este caso la raíz y le damos a **Done**.


![1][Clonar8]





Nos pedirá que le demos a **Enter** para confirmar.


![1][Clonar9]





# Clonación del Disco {#header1}



Aqui podemos seleccionar el modo en el que deseamos continuar, yo usare **Beginner** que es mas que suficiente para hacer clonaciones de disco

![1][Clonar10]





Seleccionamos **savedisk** ya que lo que deseamos hacer es clonar el disco no una particion.


![1][Clonar11]





Introducimos el nombre que tendrá la copia de seguridad, es aconsejable mantener la estructura: *YY-MM-DD-SO-NOMBRE* para una mayor claridad a la hora de revisar las copias de seguridad.

![1][Clonar12]





Seleccionamos cual es el disco que queremos clonar, aquí nunca saldrá el disco que hemos montado anteriormente para guardar la copia, en este caso el disco que queremos clonar es **sda**.


![1][Clonar13]





Aquí nos empezara a pedir unas configuraciones básicas, mi recomendación es dejarlas todas por defecto, la opción por defecto es **-sfsck** para saltar la revisión y reparación de la copia una vez que se ha hecho.

![1][Clonar14]





Después nos preguntara si queremos comprobar si la imagen creada es restaurable, la opción recomendada es **Yes, check the saved image**

![1][Clonar15]





Indicamos que cuando termine se apague con **poweroff**, ya que es un proceso largo y posiblemente no estemos cuando termine de clonarse.

![1][Clonar16]





Nos muestra el comando que se va a ejecutar por si queremos usarlo la próxima vez automatizando todo el proceso.

![1][Clonar17]





Nos muestra lo que se va a hacer y nos pide confirmación para proceder a hacer la copia.

![1][Clonar18]





Empieza el proceso de clonado de cada partición de **sda** en una carpeta de **sdb** y cuando termine apagara el equipo.

![1][Clonar19]



[Clonar1]: /images/2018/ClonezillaClonar/1_ClonezillaClonar.png
[Clonar2]: /images/2018/ClonezillaClonar/2_ClonezillaClonar.png
[Clonar4]: /images/2018/ClonezillaClonar/4_ClonezillaClonar.png
[Clonar5]: /images/2018/ClonezillaClonar/5_ClonezillaClonar.png
[Clonar6]: /images/2018/ClonezillaClonar/6_ClonezillaClonar.png
[Clonar7]: /images/2018/ClonezillaClonar/7_ClonezillaClonar.png
[Clonar8]: /images/2018/ClonezillaClonar/8_ClonezillaClonar.png
[Clonar9]: /images/2018/ClonezillaClonar/9_ClonezillaClonar.png
[Clonar10]: /images/2018/ClonezillaClonar/10_ClonezillaClonar.png
[Clonar11]: /images/2018/ClonezillaClonar/11_ClonezillaClonar.png
[Clonar12]: /images/2018/ClonezillaClonar/12_ClonezillaClonar.png
[Clonar13]: /images/2018/ClonezillaClonar/13_ClonezillaClonar.png
[Clonar14]: /images/2018/ClonezillaClonar/14_ClonezillaClonar.png
[Clonar15]: /images/2018/ClonezillaClonar/15_ClonezillaClonar.png
[Clonar16]: /images/2018/ClonezillaClonar/16_ClonezillaClonar.png
[Clonar17]: /images/2018/ClonezillaClonar/17_ClonezillaClonar.png
[Clonar18]: /images/2018/ClonezillaClonar/18_ClonezillaClonar.png
[Clonar19]: /images/2018/ClonezillaClonar/19_ClonezillaClonar.png


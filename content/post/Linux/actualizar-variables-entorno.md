---
title: Actualizar variables entorno
description: El objetivo es modificar el path del sistema operativo. El PATH es la variable del sistema que utiliza el sistema operativo para buscar los ejecutables necesarios desde la línea de comandos o la ventana Terminal.
date: 2015-12-16
lastmod: 2015-12-16
slug: actualizar-variables-entorno
image: "covers/linux.png"
tags:
  - windows
  - linux
  - path
categories:
  - Linux
---



## Introducción:

El objetivo es modificar el path del sistema operativo.
El PATH es la variable del sistema que utiliza el sistema operativo para buscar los ejecutables necesarios desde la línea de comandos o la ventana Terminal.
La variable del sistema PATH se puede establecer utilizando la utilidad de sistema en el panel de control de Windows o en el archivo de inicio del shell en Linux y Solaris.


## Linux

Para consultar todas las variables de entorno, Linux dispone del comando `env`

Algunas variables importantes son:

```bash
SHELL=/bin/bash        (el tipo de shell en uso)
TERM=xterm             (el programa de terminal por defecto)
USER=pi                (el nombre de usuario)
PWD=/home/pi           (la ruta por defecto del usuario)
LANG=es_ES.utf8        (el juego de caracteres de idioma)
DESKTOP_SESSION=KDE    (el entorno de escritorio)
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin      (el PATH)
```

Para consultar el valor de una en particular usamos `echo`
```bash
echo $PATH
```

#### ¿Dónde están los archivos de configuración del PATH?

Los archivos globales del sistema están en:
```bash
/etc/profile
/etc/profile.d/
/etc/.bashrc
```

y los archivos del espacio de usuario:
```bash
~/.bashrc
~/.bash_profile
~/.zshrc
```


### Consola

Tenemos dos formas de modificar el PATH, una fija y otra temporal que se borrara una vez que se apague el sistema

#### Forma temporal

Por la terminal introducimos el comando:
```bash
PATH=/opt/test/:$PATH
```
Donde Tenemos que cambiar `/opt/test/` por el directorio que queramos meter dentro del PATH

#### Forma fija

1. Edite el archivo de inicio (~/.bashrc)
2. Modifique la variable PATH
    ```bash
    PATH=/opt/test/:$PATH
    ```
3. `export PATH`
4. Guarde y cierre el archivo


## Windows

Windows permite modificar el PATH tanto graficamente como por consola.


###Consola

```bash
SET PATH=%PATH%;C:\Program Files\Java\jdk1.8.0_65\bin
```

### Gui

1. En Buscar, busque y seleccione: Sistema (Panel de control)
2. Haga clic en el enlace Configuración avanzada del sistema.
3. Haga clic en Variables de entorno. En la sección Variables del sistema, busque la variable de entorno PATH y selecciónela. Haga clic en Editar. Si no existe la variable de entorno PATH, haga clic en Nuevo.
4. En la ventana Editar la variable del sistema (o Nueva variable del sistema), debe especificar el valor de la variable de entorno PATH. Haga clic en Aceptar. Cierre todas las demás ventanas haciendo clic en Aceptar.
5. Vuelva a abrir la ventana del indicador de comandos y ejecute el código de java.





Fuentes: [0][java] [1][0]
[java]: https://www.java.com/es/download/help/path.xml
[0]: https://rootsudo.wordpress.com/2014/04/06/el-path-la-ruta-de-linux-variables-de-entorno/

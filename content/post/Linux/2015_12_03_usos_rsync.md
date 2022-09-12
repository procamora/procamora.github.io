---
title: Uso de Rsync
description: 
date: 2015-12-03
lastmod: 2015-12-03
slug: 2015_12_03_usorsync
image: "covers/linux.png"
tags:
  - rsync
  - command
categories:
  - Linux
---


rsync es una herramienta para sincronizar los ficheros y directorios que tenemos almacenados en un sitio en otro diferente minimizando la transferencia de datos

###Uso:

`rsync [OPTION] SRC DEST`

###Opciones básicas
```
-r: Modo recursivo.
-l: Mantiene los enlaces simbólicos.
-p: Mantiene los permisos en archivos y subdirectorios.
-t: Mantiene la hora y fecha.
-g: Mantiene el grupo.
-o: Mantiene el dueño (owner).
-D: Mantiene los archivos de dispositivo (root).
-a: Es el modo Archive. (Usar a es lo mismo que poner -rlptgoD).

-t: Preserva los tiempos de modificación de los archivos que están siendo transferidos.
-q: Suprime todos los mensajes que no sean de error,es contrario a -v.
-d: Copia los archivos de un directorio sin utilizar recursividad para copiar los directorios internos.
-l: Copia los symlinks como symlinks
-L: Copia los archivo a los que un symlink está apuntando cuando encuentre un symlink.
-W: Copia archivos enteros, cuando utilizamos el algoritmo de delta-transfer solo se copia la parte de un archivo que fue actualizada.
-h: Muestra la información que provee rsync en un formato más legible (K's, M's, G's). 
-m: No envía los directorios vacíos.
-z: Comprimirá el bloque antes de pasarlo.
-n: El comando no haga nada en realidad, se usa para ve si esta bien el script.

–upDate:    Actualiza los ficheros en el destino SÓLO si el origen de la copia han sido modificados
--progress: Muestra el progreso de los archivos que están siendo transferidos.
--delete:   Borra archivos directorio destino si han sido borrados en origen (sincronizas)

--exclude=PATTERN:   Excluir archivos que coinciden con la expresión PATTERN
--exclude-from=FILE: Obtener el conjunto de expresiones del archivo especificado por FILE
--include=PATTERN:   No excluir los archivos que coinciden con la expresión PATTERN
--include-from=FILE: Obtener el conjunto de expresiones del archivo especificado por FILE
--files-from=FILE:   Incluir los archivos especificados en el archivo FILE

```

####include-from
    el carácter + indica incluir
    el carácter - indica excluir
    / matchea con el directorio /
    /* matchea con todos los archivos en /
    /** matchea con todos los archivos y directorios en /
    /*** matchea con todos los archivos y directorios en / e incluso también con /
    el - * al final indica que lo que no ha sido aceptado hasta entonces se excluya

```
+ */
+ /etc/ssh/*
+ /var/log/*
- *
```
####exclude-from
```
*.lnk
*.regtrans-ms
*.DAT*
*.dat*
*.LOG*
*.log*
```

###Pc local a pc remoto

Copia archivos mientras muestra el progreso para cada copia.
```bash
rsync -avz --progress /tmp/ user@server.com:/home/pi/algo/
```

Copia los archivos inferiores en tamaño a 10Mb y superiores a 1MB.
```bash
rsync -avz --max-size='10240k' --min-size='1024k' ~/Documentos user@server.com:/home/pi/algo/`
```

###Pc remoto a pc local

Excluye todos los archivos y directorios excepto los de tipo .zip.
```bash
rsync -avz --exclude='*' --include='*.zip' user@server.com:/home/pi/algo/ /media/hd2/mibackup
```
 
Todos los datos se copian y transfieren cifrados sobre ssh.
```bash
rsync -avze ssh user@server.com:/home/pi/algo/ /media/hd2/mibackup/
```

###Local
El que uso habitualmente
Copia archivo en modo Archive para sincronizar directorios
Muestra el progreso para cada copia
Muestro información mas legible, no envió directorios vacíos
```bash
rsync -av -hm --delete --progress --exclude-from 'exclude.txt' "/cygdrive/c/Users/" /cygdrive/l/BackUp/
```


###Rsync con clave privada
#EN PROCESO
http://troy.jdmz.net/rsync/index.html

##Importante
1. Respecto a cómo pasarle los nombres de los directorios, hay que tener una especial atención respecto a si ponemos una barra al final del nombre del directorio o no, ya que significan cosas distintas:

    ```bash
    rsync -av /src/foo /dest       =>  /path/foo significa "el directorio foo"
    rsync -av /src/foo/ /dest/foo  => /path/foo/ significa "lo que hay dentro de foo"
    ```

2. En windows en vez de escribir `C:\`  -> `/cygdrive/c/` .

3. Usar siempre rutas absolutas.

4. usar el parámetro `-n` para evitar eliminar archivos no deseados, el comando no hace nada.

Fuente: [0][0] [1][1]

[0]: http://blog.elhacker.net/2014/02/ejemplos-rsync-para-hacer-copias-de-seguridad-remotas-backup.html
[1]: http://www.vicente-navarro.com/blog/2008/01/13/backups-con-rsync/
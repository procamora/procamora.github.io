---
title: Gestión de usuarios y grupos ftp
description: 
date: 2015-11-01
lastmod: 2015-11-01 
slug: usuarios_grupos
image: "covers/linux.png"
tags:
  - ftp
categories:
  - Linux
---


###### Creamos el usuario:
`sudo useradd -G ftp -d /home/ftp/rocky -c "Nombre y Apellidos" rocky`
```
-G ftp El usuario pertenece al grupo FTP
-d /home/ftp/pedro Es el directorio de trabajo del usuario
-c "Nombre y Apellidos" Es un comentario del usuario
-s /bin/bash Es el shell que usara el usuario
```

###### Asignamos una contraseña para el usuario
`sudo passwd rocky`


###### Modificar un usuario
`sudo usermod -s /bin/ftp rocky`

```
-c añade o modifica el comentario /etc/passwd
-d modifica el directorio de trabajo del usuario
-g cambia el número de grupo principal del usuario (GID)
-G establece otros grupos a los que puede pertenecer el usuario, separados por comas.
-l cambia el login o nombre del usuario
-L bloque la cuenta del usuario, no permitiéndole que ingrese al sistema.
-s cambia el shell por defecto del usuario cuando ingrese al sistema.
-u cambia el UID del usuario.
-U desbloquea una cuenta previamente bloqueada con la opción -L.
```


###### Borrar un usuario de etc/passwd y /etc/shadow
`sudo userdel nombre_usuario`


###### Borrar un usuario de etc/passwd /etc/shadow y su carpeta personal
`sudo userdel -r nombre_usuario`


###### Un usuario de etc/passwd /etc/shadow su carpeta personal aunque el usuario este logueado en el sistema
`sudo userdel -f nombre_usuario`


###### Crear un grupo de usuarios
`sudo groupadd nombre_grupo`

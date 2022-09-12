---
title: Comandos básicos
description: 
date: 2015-11-15
lastmod: 2015-11-15
slug: comandos_basicos
image: "covers/linux.png"
tags:
  - commands
  - apt
categories:
  - Linux
---


`adduser`: Se utiliza para añadir un usuario.

*Uso: adduser <nombreusuario>

`Alias` (este esta bien explicado en un post anterior)

*Uso: alias nombrequeledamos=’comando’*

`apt-get install nombredelprograma` =  instala el paquete.

`apt-get remove nombredelprograma` = Borra el paquete. Con la opción –purge borra también la configuración del paquete instalado.

`apt-get update` = Actualiza la lista de paquetes disponibles para instalar.

`apt-get upgrade`  = Instala las nuevas versiones de los diferentes paquetes disponibles.

`cd` = Cambia el directorio.

*Uso: cd nombredirectorio*

Continuar leyendo el resto de comandos:

`chmod`: Cambia los permisos de los archivos.

r:lectura w:escritura x:ejecución
+: añade permisos -:quita permisos
u:usuario g:grupo del usuario o:otros
*Uso: chmod permisos nombrearchivo*

`chown`: Cambia el propietario de un archivo.

*Uso: chown <nombrepropietario> <nombrearchivo>*

`cp`:Copia archivos en el directorio indicado.

*Uso: cp archivoorigen archivodestino*

`deluser`: Elimina una cuenta de usuario

*Uso: deluser <nombreusuario>*

`exit`: Cierra las ventanas o las conexiones remotas establecidas

`fsck`: Sirve para chequear si hay errores en nuestro disco duro.

*Uso: fsck -t <fs_typo> <dispositivo>*

`ftp`: Protocolo de Transferencia de Archivos, permite transferir archivos de y para computadores remotos.

*Uso: ftp <maquina_remota>*

`grep`: Su funcionalidad es la de escribir en salida estándar aquellas líneas que concuerden con un patrón. Busca patrones en archivos.

grep: grep <patronabuscar> <nombrearchivos>

`ifconfig`: Obtener información de la configuración de red

`kill`: Termina un proceso

*Uso: kill numeroPID*

`ls`:Lista los archivos y directorios dentro del directorio de trabajo.

`make`: Crea ejecutables a partir de los archivos fuente.

`man`: muestra el manual de un programa o comando si este esta disponible

*Uso: man <nombredelcomando>*


`mkdir`: Crea un nuevo directorio.

*Uso: mkdir nombredirectorio*


`mount`: Monta una unidad.

*Uso: mount -t< sistema_de_archivo> <dispositivo> <nombredirectorio>*


`mv`: Este comando sirve para renombrar un archivo.

*Uso: mv <nombrearchivo> <nuevonombrearchivo>*


`netstat`:Muestra las conexiones y puertos abiertos por los que se establecen las comunicaciones.


`poweroff`: Apaga el ordenador.


`ps`: Muestra información acerca de los procesos activos.


`rlogin`: Conecta un host local con un host remoto.

*Uso: rlogin <maquina_remota>*


`rm`: Remueve o elimina un archivo.

*Uso: rm <rutaynombrearchivo>*


`rmdir`: Elimina el directorio indicado, el cual debe estar vacío.

*Uso: rmdir nombredirectorio*


`sudo` o `su`: Con este comando accedemos al sistema como root.

`umount`: Desmontar unidades montadas anteriormente

*Uso: umount <nombredirectorio>*


`wc`:Cuenta los caráteres, palabras y líneas del archivo de texto.

*Uso: wc nom_archivo*


`whereis`: Devuelve la ubicación del archivo especificado, si existe.

*Uso: whereis nomb_archivo*

---
title: Configurar pure-ftpd
description: 
date: 2015-08-03
lastmod: 2015-08-03
slug: pure_ftpd
image: "covers/software.png"
tags:
  - linux
  - ftp
  - pureftpd
categories:
  - Software
---





###### 0. Instalar los paquetes necesarios
`apt-get install pure-ftpd pureadmin`


###### 1. Creación de un usuario y grupo para el FTP
`sudo groupadd ftpgroup`

`sudo useradd -g ftpgroup -d /dev/null -s /etc ftpuser`


###### 2. Creación de un directorio para el FTP
`sudo mkdir /home/ftp`


###### 3. Creación de un usuario FTP
`sudo pure-pw useradd usuario -u ftpuser -d /home/ftp`


###### 4. Creación de base de datos del usuario
`sudo pure-pw mkdb`


###### 5. Hacemos un link al archivo PureDB
`sudo ln -s /etc/pure-ftpd/conf/PureDB /etc/pure-ftpd/auth/PureDB`


###### 6. Denegamos acceso a anonymous
`sudo echo yes > /etc/pure-ftpd/conf/NoAnonymous`


###### 7. Denegamos autenticación PAM
`sudo echo no > /etc/pure-ftpd/conf/PAMAuthentication`


#####Algunas configuraciones adicionales serían:
###### 8. Limitar el número de usuarios
`sudo echo 10 > /etc/pure-ftpd/conf/MaxClientsNumber`


###### 9. No permitir mostrar los ficheros ocultos
`sudo echo no > /etc/pure-ftpd/conf/DisplayDotFiles`


###### 10. Denegar lectura y escritura de ficheros ocultos
`sudo echo yes > /etc/pure-ftpd/conf/ProhibitDotFilesRead`

`sudo echo yes > /etc/pure-ftpd/conf/ProhibitDotFilesWrite`


###### 11. Prohibimos ejecución de chmod
`sudo echo yes > /etc/pure-ftpd/conf/NoChmod`


###### 12. Reiniciamos el servicio
`sudo invoke-rc.d pure-ftpd restart`


######11. Verificamos que la configuración concuerde con la que hicimos
`sudo pure-pw show usuario`


Y ya podemos disfrutar de nuestro FTP!



El monitoreo puede ser por consola a gráficamente

`sudo pure-ftpwho`
`sudo pureadmin`

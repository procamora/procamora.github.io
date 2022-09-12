---
title: Uso de rc.local
description: Debajo de */etc* se encuentra el directorio **rc.d** que a la vez contiene un directorio para cada nivel de ejecución, así tenemos *rc0.d*, *rc1.d*, *rc2.d*, *rc3.d*, etc.
date: 2015-11-02
lastmod: 2015-11-02
slug: rc_local
image: "covers/linux.png"
tags:
  - console
  - init.d
categories:
  - Linux
---


## Los directorios rc

Debajo de */etc* se encuentra el directorio **rc.d** que a la vez contiene un directorio para cada nivel de ejecución, así tenemos *rc0.d*, *rc1.d*, *rc2.d*, *rc3.d*, etc. Hay algunas distros que estos directorios están ubicados directamente en */etc*. Como ya te imaginaras, cada uno de estos directorios contiene scripts (o mas bien enlaces a scripts) que apuntan al directorio *init.d*, entonces el comando init (ya sea ejecutado manualmente o cuando se inicia el sistema), dependiendo del nivel indicado leerá cada uno de los enlaces o accesos directos del directorio respectivo.

Ahora bien, un ejemplo (parcial) típico de estos directorios puede ser el siguiente, tomado de rc3.d
```
lrwxrwxrwx   1 root root    7 Oct 20 20:05 K22dbus -> ../init.d/dbus
lrwxrwxrwx   1 root root    9 Oct 20 20:05 K22resmgr -> ../init.d/resmgr
lrwxrwxrwx   1 root root    8 Oct 20 20:05 K24fbset -> ../init.d/fbset
lrwxrwxrwx   1 root root    9 Oct 20 20:05 K24random -> ../init.d/random
lrwxrwxrwx   1 root root    8 Oct 20 18:23 S01fbset -> ../init.d/fbset
lrwxrwxrwx   1 root root    9 Oct 20 18:22 S01random -> ../init.d/random
lrwxrwxrwx   1 root root    7 Oct 20 18:29 S03dbus -> ../init.d/dbus
lrwxrwxrwx   1 root root    9 Oct 20 18:23 S03resmgr -> ../init.d/resmgr
lrwxrwxrwx   1 root root   12 Oct 20 18:24 S04boot.udev -> ../init.d/boot.udev
lrwxrwxrwx   1 root root   10 Oct 20 21:16 S05network -> ../init.d/network
lrwxrwxrwx   1 root root    9 Oct 20 18:23 S06syslog -> ../init.d/syslog
```


Nótese que todos son enlaces al directorio init.d que como ya se vio previamente es donde realmente están ubicados los scripts de arranque de los servicios o servidores. También, todos los enlaces comienzan con K (kill) o con S (start), es pues fácil deducir que los que comienzan con K son scripts que recibirán el argumento stop y los que comienzan con S el de start, es decir, se inician. Esta gran simplicidad ofrece una enorme potencia al momento de configurar servicios ya que basta con agregar o quitar enlaces con el formato indicado para personalizar los niveles de ejecución a nuestro gusto.

Después de la K o S sigue un número consecutivo, seguido generalmente del nombre del servicio que afectan, el número secuencial es simplemente el orden en que se leerán los scripts, primero los K comenzando con el 01 y hacía adelante y después los S. Entonces si por ejemplo no queremos que se inicie el samba en el nivel 3 bastaría con borrar su enlace en este directorio:

`pwd`
```
/etc/rc.d/rc3.d
```

`rm S54smb`

Y listo, el servidor samba ya no arrancaría cuando entremos en este nivel de ejecución. Si por lo contrario lo que deseamos es iniciar (o apagar) un servicio, basta con crear su enlace en el directorio respectivo:

`pwd`
```
/etc/rc.d/rc5.d
```

`ln -s /etc/rc.d/init.d/mysql S90mysql

`ls -l S90mysql
```
lrwxrwxrwx   1 root root    9 Oct 20 18:23 S90mysql -> ../init.d/mysql
```

Con esto la siguiente vez que iniciemos el equipo o cambiemos a nivel 5 con init, también se iniciará el servidor de la base de datos MySQL. El número 90 es escogido al azar entre 01 y 99 es simplemente el orden en que serán iniciados o detenidos los servicios.

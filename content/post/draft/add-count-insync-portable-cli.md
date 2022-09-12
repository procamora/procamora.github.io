---
title: Add count insync portable cli
description: 
date: 2016-06-21
lastmod: 2016-06-21
slug: add-count-insync-portable-cli
image: "covers/draft.png"
tags:
  - insync
  - raspberrypi
  - arm
categories:
  - Linux
---






Para usar Insync desde la consola en Raspberry hay disponibles 2 compilaciones:

- [armhf][armhf]
- [armel][armel]


Lo primero es saber cual de las 2 versiones necesita, para ello tenemos dos opciones, ambas son leyendo


```bash
readelf -A /proc/self/exe | grep Tag_ABI_VFP_args

readelf -A /lib/arm-linux-gnueabihf/libc.so.6 | grep Tag_ABI_VFP_args
```


Si obtenemos la linea _Tag_ABI_VFP_args: VFP registers_ entonces es armhf, en caso de que no este la linea es armel.



[armhf]: /downloads/insync/insync-armhf_1.3.17.36167_i386.tar.bz2
[armel]: /downloads/insync/insync-armel_1.3.17.36167_i386.tar.bz2


Una vez que hemos descargado la build que necesitamos, en mi caso armhf



```bash
wget https://d2t3ff60b2tol4.cloudfront.net/test_builds/armhf/insync-armhf_1.3.17.36167_i386.tar.bz2
# or
wget procamora.github.io/downloads/insync/insync-armhf_1.3.17.36167_i386.tar.bz2
```


Descomprimimos el fichero descargado:


```bash
tar -xjf insync-armhf_1.3.17.36167_i386.tar.bz2
```


Accedemos al directorio que se ha creado e iniciamos el proceso:


```bash
./insync-portable start 
```


Nos pedirá que añadamos una nueva cuenta, para ello necesitamos un token de acceso a nuestra cuenta de google, esto se hace desde la siguiente url: [https://insynchq.com/auth][insynchq].

[insynchq]: https://insynchq.com/auth



```bash
./insync-portable add_account --auth-code 34/P23489sd4sHp08785548ssssswf8s7df7sdflk_KLl33235s7d8a456
```



También se puede gestionar la cuenta para descargar solo las carpetas deseadas con:


```bash
./insync-portable manage_selective_sync mail@gmail.com
```






Fuentes: [0][help], [1][forums], [2][sneakykoder]


[help]: https://help.insynchq.com/en/articles/112904-linux-insync-on-raspberry-pi
[forums]: https://forums.insynchq.com/t/how-to-test-insync-on-raspberry-pi/36
[sneakykoder]: https://sneakykoder.wordpress.com/2013/09/24/insync-google-drive-in-linux/
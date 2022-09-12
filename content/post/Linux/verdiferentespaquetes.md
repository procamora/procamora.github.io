---
title: Ver Diferentes Paquetes
description: 
date: 2015-12-06
lastmod: 2015-12-06
slug: verdiferentespaquetes
image: "covers/linux.png"
tags:
  - fedora
  - dnf
  - apt
  - debian
categories:
  - Linux
---



## PC 1 (FUNCIONAL)

### Sistemas basados en Debian

```bash
#coger todas los paquetes instalados que no sean librerías o common 
dpkg --get-selections | grep -v deinstall  | awk '{print $1}' | egrep -v '^lib.*|common' > i5.tmp
```

### Sistemas basados en Fedora
```bash
dnf list installed | awk '{print $1}' | egrep -v '^lib.*|common' > i5.tmp
```

## PC 2 (RECIÉN INSTALADO)

```bash
#!/bin/bash

#coger todas los paquetes instalados que no sean librerías o common 
dpkg --get-selections | grep -v deinstall  | awk '{print $1}' | egrep -v '^lib.*|common' > i7.tmp

diff i5.tmp i7.tmp > test.tmp

#limpieza de lineas innecesarias creadas por diff
#egrep -v '[0-9]+[a-z]+[0-9]+' test.tmp > test2.tmp # otra forma de sacar las diferencias
sed -Ei '/[0-9]+[a-z]+[0-9]+|> |---/d' test.tmp # con -e no funciona, investigar

# poner los sudo
sed -i 's/< /sudo apt-get -y install /g' test.tmp

bash test.tmp
```


EN UN FUTURO HACER UN SCRIPT PASANDO PARÁMETRO PARA HACER USARLO


script.py -p origen
script.py -p destino
script.py -o instalar
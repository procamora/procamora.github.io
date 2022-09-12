---
title: autorun script linux systemd
description: Crear un script que arranque con el sistema.
date: 2016-03-24
lastmod: 2016-03-24
slug: autorun-script-linux-systemd
image: "covers/linux.png"
tags:
  - raspberrypi
  - systemd
categories:
  - Linux
---





## Paso 1: Crear el fichero del servicio.

```bash
sudo vim /lib/systemd/system/myscript.service
```


## Paso 2: Añadir el contenido al fichero.

```bash
[Unit]
Description=My Script Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/pi/myscript.py > /home/pi/myscript.log 2>&1
User=pi

[Install]
WantedBy=multi-user.target
```

## Paso 3: Poner los permisos necesarios al fichero.

```
sudo chmod 644 /lib/systemd/system/myscript.service
```


## Paso 4: Configurar systemd.

```
sudo systemctl daemon-reload
sudo systemctl enable myscript.service
```

## Paso 5: Reiniciar el sistema.

```
sudo reboot
```


## Paso 6: Confirmar que el servicio esta funcionando.


```
sudo systemctl status myscript.service
```






Fuentes: [raspberrypi][0] [archlinux][1]




[0]: http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/
[1]: https://wiki.archlinux.org/index.php/Systemd_%28Espa%C3%B1ol%29

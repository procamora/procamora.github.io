---
title: Usar vlc como root
description: Cuando ejecutas linux como root obtienes el siguiente resultado
date: 2016-01-29
lastmod: 2016-01-29
slug: 2016_01_09_usar-vlc-como-root
image: "covers/software.png"
tags:
  - vlc
  - linux
  - kali
categories:
  - Software
---


Cuando ejecutas linux como root obtienes el siguiente resultado:

```
VLC is not supposed to be run as root. Sorry.
If you need to use real-time priorities and/or privileged TCP ports
you can use ./vlc2-wrapper (make sure it is Set-UID root and
cannot be run by non-trusted users first).
```

Para poder ejecutarlo con éxito es tan simple como abrir el binario de vlc con un editor hexadecimal y sustituir geteuid por getppid

`ghex /usr/bin/vlc`

buscar: geteuid

remplazar: getppid

<br />

Con python:
```python
#!/usr/bin/env python
# -*- coding= utf-8 -*- #

nombre_fichero = 'vlc'


with open(nombre_fichero, 'rb') as f:
	s=f.read()

s=s.replace(b'geteuid', b'getppid')

with open(nombre_fichero, 'wb') as f:
	f.write(s)
```
<br />
Con bash:
```bash
sed -i 's/geteuid/getppid/' /usr/bin/vlc
```

<br />

En caso de haber instalado vlc a través del tarball seria tan simple como recompilarlo pasando ***--enable-run-as-root***  a  ***./configure***.

Fuentes: [taringa][0]


[0]: http://www.taringa.net/posts/linux/18950109/Usar-vlc-en-Kali-Linux-como-root.html

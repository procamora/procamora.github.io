---
title: Optimizar PDF's
description: Para optimizar un pdf usaremos la herramienta _Ghostscript_ tenemos 2 formas de utilizarlo
date: 2018-01-30
lastmod: 2018-01-30
slug: optimizar-pdf
image: "covers/software.png"
tags:
  - pdf
  - optimizar
  - linux
categories:
  - Software
---

Para optimizar un pdf usaremos la herramienta _Ghostscript_ tenemos 2 formas de utilizarlo: para un unico fichero o en un directorio.


Optimizar un pdf:

`optimiza_pdf.sh fichero.pdf`

Optimizar todos los pdf que hay en un directorio:

`find . -type f -name "*.pdf" -exec ./optimiza_pdf.sh {} \;`


```bash
#!/bin/bash
#Script para optimizar pdf se para como argumento el pdf
# para ejecutarlo sobre un directorio find . -type f -name "*.pdf" -exec ./optimiza_pdf.sh {} \;

TEMP="temporal.pdf"

echo "$1"
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$TEMP" "$1"
mv "$TEMP" "$1"
```

Puedes descargar el script [pulsado aqui][script]


[script]: /code/optimiza_pdf.sh


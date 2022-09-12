---
title: Guia Básica Pelican
description: 
date: 2015-11-30
lastmod: 2015-11-30
slug: guiabasicapelican
image: "covers/draft.png"
tags:
  - pelican
  - python
categories:
  - Software
---



http://docs.getpelican.com/en/stable/content.html

http://docs.getpelican.com/en/stable/publish.html

http://docs.getpelican.com/en/stable/tips.html

http://spapas.github.io/2013/10/07/pelican-static-windows/


Para ver las opciones hacer un:

`make`


`$ ~/projects/pagina $ make devserver`

`$ ~/projects/pagina $ make stopserver`

 ~/projects/pagina $ pelican -s pelicanconf.py
 python -m pelican.server



http://www.pelicanthemes.com/



## Modifying pelican tools for windows

Pelican uses a Makefile and a unix shell script to generate the static html files and start an http server for development. Because I prefer to use windows, I answered no to the questions of generating these when pelican-quickstarte asked me. Instead I have included the following files inside the spapas.github.io directory:

pelrun.bat, to generate the content for your debug site in the output directory:

`pelican content --debug --autoreload  --output output --settings pelicanconf.py`

pelserve.bat, to localy serve the generated debug site:

```
pushd output
python -m pelican.server
popd
```
pelpub.bat, to generate the production site in the output directory:

`pelican content --output output --settings publishconf.py`

Now, when you want to develop your site locally, enter:

spapas.github.io>start pelrun.bat
spapas.github.io>start pelserv.bat

If everything was ok until now, you can visit http://127.0.0.1:8000 and will get the following output:


Fuentes: [1][0]

[0]: http://joedicastro.com/pelican-publicacion-y-automatizacion.html
[1]: http://joedicastro.com/optimizar-imagenes-para-la-web.html

---
title: Configuración vim
description: En ocasiones en las que hay que trabajar con ficheros yaml o similares (netplan, Dockerfile, docker-compose, etc) que son sensibles a la identación, puede ser interesante modificar vim para que ponga un tabulado de espacios y con la cantidad de espacios deseado, esto se realiza de la siguiente forma.
date: 2020-03-15
lastmod: 2020-03-15
slug: configuracion_vim
image: "covers/htb.png"
tags:
  - linux
  - vim
categories:
  - Software
---



En ocasiones en las que hay que trabajar con ficheros yaml o similares (netplan, Dockerfile, docker-compose, etc) que son sensibles a la identación, puede ser interesante modificar vim para que ponga un tabulado de espacios y con la cantidad de espacios deseado, esto se realiza de la siguiente forma:





```
:filetype plugin indent on

# Forzamos a que la identacion sea de 2 caracteres (espacios)
:set shiftwidth=2
:set expandtab
```





También puede ser interesante activar una especie de "modo debug" en la que ver todos los caracteres especiales, esto se activaría de la siguiente forma:



```
:set listchars=eol:¬,tab:>·,trail:~,extends:>,precedes:<,space:␣
:set list
```




Fuentes: [0][ident], [1][show_chars]


[ident]: https://stackoverflow.com/questions/234564/tab-key-4-spaces-and-auto-indent-after-curly-braces-in-vim
[show_chars]: https://stackoverflow.com/questions/1675688/make-vim-show-all-white-spaces-as-a-character
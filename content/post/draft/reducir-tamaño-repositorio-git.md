---
title: Reducir tamaño repositorio git
description: Para comprimir el tamaño de un repositorio git podemos usar los siguientes comandos
date: 2019-04-27
lastmod: 2019-04-27
slug: reducir-tamano-repositorio-git
image: "covers/draft.png"
tags:
  - git
categories:
  - Software
---



Para comprimir un repositorio git y reducir su tamaño podemos usar los siguientes comandos:


```bash
git reflog expire --all --expire=now
git gc --prune=now --aggressive
```



Fuente: [0][sf1]

[sf1]: https://stackoverflow.com/questions/2116778/reduce-git-repository-size
---
title: 
description: 
date: 
lastmod: 
slug: 
image: "covers/software.png"
tags:
  - 
categories:
  - Software
---

Title: Problema al instalar Mdcharm en linux
Date: 2015-12-26 2:15
Modified: 2015-12-26 20:33
Category: Software
Tags: consola, mdcharm
Slug: mdcharmlinux
Summary: Al instalar Mdcharm en linux y ejecutarlo obtengo este mensaje.
Status: published

Al instalar Mdcharm en linux y ejecutarlo obtengo este mensaje.

`$ mdcharm`

*mdcharm: error while loading shared libraries: libhunspell.so: cannot open shared object file: No such file or directory*



se soluciona instalando estos paquetes

```bash
sudo apt-get install libhunspell-1.3-0 libhunspell-dev
```


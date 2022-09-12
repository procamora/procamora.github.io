---
title: Export EasyEda
description: Aquí se va a explicar como exportar el esquemático y el PCB como imágenes, si se quieren usar para diseñar un PCB sera necesario espejar la imagen y aquí no se explica por el momento.
date: 2019-10-30
lastmod: 2019-10-30
slug: export-easyeda
image: "covers/software.png"
tags:
  - easyeda
  - svg
  - png
  - pdf
categories:
  - Software
---

Aquí se va a explicar como exportar el esquemático y el PCB como imágenes, si se quieren usar para diseñar un PCB sera necesario espejar la imagen y aquí no se explica por el momento.


# Exportar Esquemático

Para exportar el esquemático se puede hacer en formato SVG de la forma:


File > Exportar > SVG > Exportar


Una vez que esta localmente, se podría convertir a formato PDF en caso deseado usando Inkscape, de la forma:


```bash
inkscape --file=Schematic.svg --export-area-drawing --without-gui --export-pdf=Schematic.pdf
```

Tambien se puede convertir a formato PNG aumentando el DPI para mejorar la calidad, de la forma:

```bash
inkscape -f=Schematic.svg --export-area-drawing --without-gui --export-png=Schematic.png \
--export-dpi=800
```


# Exportar PCB


A la hora de exportar el PCB, si se intenta exportar en formato SVG obtendremos una imagen completamente negra, no se el motivo, por lo que se tendrá que exportar en formato PDF para mantener una calidad buena.


File > Exportar > PDF

Aquí habrá que realizar un configuración antes de exportar, que será la siguiente:

- Graphics: Full Graphics
- Type: Capa fusionada
- Color: Full Color


[jtable caption="This is caption" th="0"]
Capas,Exportar
Capa superior,Si
Capa inferior,Si
Capa de serigrafia superior,Si
Capa de serigrafia inferir,Si
Bordes de placa,Si
Multi-Layer,Si
Orificio,Si
[/jtable]



Una vez que esta en formato PDF se puede convertir a formato PNG de la siguientes formas:


```bash
inkscape -f=Schematic.pdf --export-area-drawing --without-gui --export-png=Schematic.png \
--export-dpi=800

convert -density 800 Schematic.pdf Schematic.png
```



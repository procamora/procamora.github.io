---
title: Concatenar pdf
description: El objetivo es concatenar múltiples pdf en un único pdf, intentando mantener la estructura interna de los pdf a unir.
date: 2016-05-11
lastmod: 2016-05-11
slug: concatenar-pdf
image: "covers/software.png"
tags:
  - markdown
  - pdf
  - pdfunite
  - gs
  - markdown
  - linux
  - ghostscript
  - pdfjam
  - imagemagick
  - smallpdf
  - python
  - pypdf2
categories:
  - Software
---


# Introducción:

El objetivo es concatenar múltiples pdf en un único pdf, intentando mantener la estructura interna de los pdf a unir.



Para hacer esto tenemos múltiples opciones:

- [Concatenar por linea de comandos](#header1):
    - [pdfunite](#mark0)
    - [ImageMagick](#mark1)
    - [pdfjam](#mark2)
    - [Ghostscript Pad](#mark3)
- [Concatenar con librerias externas](#header2):
    - [Python](#mark4)
- [Concatenar Online](#header3):
    - [smallpdf](#mark5)
- [Resumen general](#header4)
- [Conclusion final](#header5)



# Concatenar por linea de comandos {#header1}

- [pdfunite](#mark0)
- [ImageMagick](#mark1)
- [pdfjam](#mark2)
- [Ghostscript Pad](#mark3)


## Pdfunite {#mark0}

[Pdfunite][pdfunite] es una herramienta muy simple excrita en ruby para unir pdf, se instala rápido, funciona bien pero el indice de los pdf se lo carga.


[pdfunite]: https://github.com/mtgrosser/pdfunite

### Instalación.

Solo hay que instalar el paquete `poppler` que lo contiene.

```
dnf install poppler-utils
```

### Unión de pdf.

Para unir varios pdf lo único que hay que hacer es pasárselos a pdfunite como argumento teniendo en cuenta que se irán añadiendo al pdf en el mismo orden y que el ultimo parámetro debe de ser el nombre del pdf resultante.

```
pdfunite pdf1.pdf pdf2.pdf output.pdf
```

Como inconveniente el indice que traigan otros pdf se lo carga.


## ImageMagick (no recomendado) {#mark1}

Este método funciona pero reduce la calidad (resolucion) del pdf un poco y aumenta bastante el tamaño del pdf resultante, su uso seria el siguiente:

```
convert -density 300x300 -quality 100 pdf1.pdf pdf2.pdf output.pdf
```

## Pdfjam  {#mark2}

[Pdfjam][pdfjam] es un conjunto de pequeños script para hacer modificaciones a pdf, pero a nosotros la única herramienta que nos interesa ahora mismo es pdfjam que es la principal, ya que es la que usaremos para unir los pdf.


[pdfjam]: http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic-research/firth/software/pdfjam/

### Instalación.

La Instalación en Fedora es simple, solo hay que instalar un paquete.

```
[sudo] dnf install  pdfjam
```

### Union de pdf.

Para unir varios pdf lo único que hay que hacer es pasárselos a pdfjam como argumento teniendo en cuenta que se irán añadiendo al pdf en el mismo orden y que el pdf resultante debe ir precedido por un `-o` para indicar que es la salida.

```
pdfjam pdf1.pdf pdf2.pdf -o output.pdf
```
Como inconveniente el indice que traigan otros pdf se lo carga.



## Ghostscript {#mark3}
Ghostscript es un paquete que te permite ver o imprimir archivos PostScript y PDF en otros formatos o a partir de estos a otros formatos, pero a demás de todo eso también te permite unir archivos pdf. La instalación no es necesaria al menos en Fedora 24 ya que venia instalado por defecto.

### Unión de pdf.
En este apartado al ser una herramienta bastante completa podríamos hacerlo de múltiples formas, antes de ponerla pondré algunos parámetros importantes que pasaremos a Ghostscript:

- -dBATCH: una vez que Ghostscript procesa los archivos PDF, debe salir. Si no incluye esta opción, Ghostscript seguirá ejecutándose.
- -dNOPAUSE: obliga a Ghostscript a procesar cada página sin pausar la interacción del usuario.
- -q: para que Ghostscript no muestre mensajes mientras funciona.
- -sDEVICE=pdfwrite: le dice a Ghostscript que use su escritor de PDF incorporado para procesar los archivos.
- -sOutputFile=output.pdf: le dice a Ghostscript que guarde el archivo PDF combinado con el nombre que especifico.


#### Unir varios pdf.

```
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=output.pdf pdf1.pdf pdf2.pdf
```

#### Unir varios pdf haciendo una pequeña compresión.

```
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile=output.pdf pdf1.pdf pdf2.pdf
```


#### Unir varios pdf haciendo una gran compresión, revisar porque puede haber perdidas de calidad visibles.

```
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/default -dCompatibilityLevel=1.4 -dQUIET -dDetectDuplicateImages -dCompressFonts=true -r150 -sOutputFile=output.pdf pdf1.pdf pdf2.pdf
```

Fuentes: [stackoverflow][stackoverflow], [linux.com][linux]

[stackoverflow]: http://stackoverflow.com/questions/2507766/merge-convert-multiple-pdf-files-into-one-pdf
[linux]: https://www.linux.com/news/putting-together-pdf-files



# Concatenar con librerías externas {#header2}

- [Python](#mark4)


## Python {#mark4}

En python podemos usar la librería pyPdf2 que depende de la librería pdf. El resultado es un pdf con el nombre `salida.pdf` que tiene buena calidad pero no mantiene los indices


> IMPORTANTE: Actualizar el script para pasarle distintos argumentos como -o para hacerlo dinamico y que no tenga un fichero de salida statico


### Instalación.

```bash
[sudo] pip install pdf pyPdf2
```

#### Unir varios pdf.


Uso: `python concatena_pdf.py portada.pdf memoria.pdf`

[Descargar script][python]

```python
#!/usr/bin/env python
from pyPdf import PdfFileReader, PdfFileWriter
import sys
#Fuente: http://stackoverflow.com/questions/3444645/merge-pdf-files

# Creating a routine that appends files to the output file
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

if len(sys.argv) == 3:
	# Creating an object where pdf pages are appended to
	output = PdfFileWriter()

	# Appending two pdf-pages from two different files
	for pdf in sys.argv[1:]:
		append_pdf(PdfFileReader(file(pdf,"rb")),output)

	# Writing all the collected pages to a file
	output.write(open("salida.pdf","wb"))
```

[python]: /code/concatena_pdf.py


# Concatenar Online {#header3}

- [smallpdf](#mark5)


## Smallpdf {#mark5}

[Smallpdf][smallpdf] es una pagina online en la que podemos hacer múltiples operaciones con pdf como unirlos, separarlos y convertirlos a múltiples formatos, funciona bastante bien pero supongo que tendrá limitaciones en cuanto al tamaño de los ficheros y el numero máximo de operaciones a hacer con una cuenta gratis/sin registrar.


[smallpdf]: https://smallpdf.com/



# Resumen general {#header4}

herramienta | mantiene integridad del indice | calidad resultante
-------|------|-------
pdfunite | &#10060; | &#10004;
ImageMagick | &#10060; | &#10060;
pdfjam | &#10060; | &#10004;
Ghostscript |  &#10004; |  &#10004;
pyPdf2 | &#10060; | &#10004;
smallpdf | &#10060; | &#10004;


# Conclusión final {#header5}

Creo que en este caso la mejor opción es Ghostscript ya que es la unica que mantiene el indice después de la unión.


Fuente: [0][0], [1][1]



[0]: http://jamesmcdonald.id.au/it-tips/alternative-to-pdftk-under-fedora-21
[1]: https://blog.dbrgn.ch/2013/8/14/merge-multiple-pdfs/

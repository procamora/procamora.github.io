---
title: Tips vim
description: 
date: 2015-08-01
lastmod: 2015-08-01
slug: tips_vim
image: "covers/software.png"
tags:
  - linunx
  - vim
categories:
  - Software
---

## Modo edición
###### habilitar la edición
`i` o `o`


## Operaciones básicas
###### Salir
`:q`

###### Salir sin confirmación
`:q!`

###### Salir guardando sin confirmación
`:wq!`

###### Guardar en un fichero x
`:w fichero.txt`

###### Cierra el actual y abre x
:e fichero.txt`


## Copiar, cortar, pegar
###### Modo visual
`v`

###### Cortar
`c`

###### Copiar
`y`

###### Pegar
`p`


## Operadores de texto
###### suprimir linea
`dd`

###### deshacer ultimo cambio
`u`

###### rehacer ultimo cambio
`CTRL+R`

###### convertir a minus la linea
`guu`

###### convertir a mayus la linea
`gUU`

###### posicionarse en linea 'num'
`:num`

###### Mostrar el número de líneas
`:set number`

###### posicionarse al principio
`gg`

###### posicionarse al final
`G`

###### Código ASCII, hex y octal
`ga`


## Búsqueda y sustitución
###### buscar
`/palabra`
>"n" o "N" para ir adelante o atras

###### remplazar
`:%s/texto1/texto2/g`
> "g" selecciona todas las coincidencias


## Comandos internos
###### Ejecutar comando interno
`:!ls`

###### Pausa en la edicion
`:shell`	despues	  `exit`

###### Compilar
`:make`	`:cc`



## Características avanzadas
###### Dividir pantalla verticalmente
`:split fichero.txt`

###### Dividir pantalla horizontalmente
`:vsplit fichero.txt`

###### Cambiar entre pantallas
`CTRL+W + flecha cursor`

###### Crear pestañas
`:tabnew fichero.txt`

###### Moverse entre pestañas
`:tabn`  o  `:tabnext`  o  `gt`

###### Sistema autocompletado
`caracter inicial + CTRL+N`

###### Elimina lineas en blanco
`:g/^\s*$/d`

###### Detecta llave mal cerrada
`{}`

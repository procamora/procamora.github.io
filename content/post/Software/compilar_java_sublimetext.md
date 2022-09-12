---
title: Compilar Java con Sublimetext 2
description: En esta entrada veremos como configurar Sublime Text 2 para que al presionar ctrl + b se compile y ejecute nuestra aplicación en java.
date: 2015-12-14
lastmod: 2015-12-14
slug: compilar_java_sublimetext
image: "covers/software.png"
tags:
  - software
  - sublimetext
  - java
categories:
  - Software
---


En esta entrada veremos como configurar Sublime Text 2 para que al presionar **ctrl + b** se compile y ejecute nuestra aplicación en java.

Lo primero que debemos hacer es iniciar Sublime Text, una vez lo hallamos hecho, vamos a `Tools -> Build System -> New Build System`... Esto abrirá un pequeño archivo con unas lineas escritas en JSON, de modo que debemos copiar el siguiente código y pegarlo en este archivo. 

En mi caso la ruta es: `%AppData%\Sublime Text 2\Packages\User`

```json
//---
title: Arduino burn bootloader
description: 
date: 
lastmod: 
slug: 
image: "covers/software.png"
tags:
  - arduino
categories:
  - Software
---

Windows y Liunx
{
	"cmd": ["javac ${file_name} && java ${file_base_name}"],
	"selector": "source.java",
	"shell" : true,
}
```

Cuando lo hallamos hecho, guardamos dicho archivo en la carpeta donde nos sugiere Sublime Text, y le ponemos un nombre descriptivo como por ejemplo java.sublime-build, **ten cuidado que la extensión del archivo sea .sublime-build.**

Y con eso ya hemos terminado, para compilar y ejecutar nuestros programas en java tan solo debes ir a `Tools -> Build System` y elegir el nombre del archivo que has modificado ante.,

Fuentes: [1][0]



[0]: http://ayudasprogramacionweb.blogspot.com.es/2012/12/compilar-y-ejecutar-java-desde-sublime-text.html
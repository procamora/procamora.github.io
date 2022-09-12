---
title: Diseño de un PCB con EasyEDA
description: 
date: 2019-12-29
lastmod: 2019-12-29
slug: diseno_de_un_pcb_con_easyeda
image: "covers/draft.png"
tags:
  - easyeda
  - pcb
categories:
  - Software
---




A continuación se va a explicar como diseñar un circuito para poder crear un PCB usando el método del planchado. Este método consiste en imprimir el circuito en un papel fotográfico para posteriormente plancharlo en una plaqueta de cobre y después mediante el uso de un ácido eliminar las partes de cobre sobrantes. Se va a partir que se tiene el circuito diseñado y creado el PCB.



# Revisión del esquema


Es recomendable realizar una serie de revisiones en el esquema para prevenir posibles errores, están son las siguientes:

- Revisar haciendo zoom para asegurarse que todos las conexiones están realizadas correctamente.
- Si hay pines no usados marcarlos como "not used".
- Poner una etiqueta en los cables para hacer mas sencilla la revisión posterior del PCB.






# Revisión en el PCB

La revisión del PCB es obligatoria antes de imprimar el PCB ya que un fallo en esta parte conllevaría una perdida de horas de trabajo.


- Revisar que el autoruteo del PCB se ha realizado correctamente.
- Revisar que todas las lineas tienen ángulos de 45° como máximo, modificando aquellas que puedan tener ángulos de 90°, ya que no es recomendable.
- Regenerar la capa de tierra, por si se ha realizado alguna modificación.
- Revisar que no hay errores en el PCB, esto se puede revisar en Design manager > DRC Errors.
- Cambiar orificios de los componentes siguiendo la siguiente tabla. Esto se debe a que aunque en el esquema salen con el orificio correcto, al crear el PCB de forma casera es recomendable modificarlos para facilitar la realización de los agujeros con la broca.


Componente | Orificio original | Orificio optimo
--------|---------|----------
Componentes 1/8W | 0.8mm | 0.6mm
Encapsulados TO-92 | 0.8mm | 0.6mm
Encapsulados DIP-8 | 0.8mm | 0.6mm
Componentes 1/4W | 1mm | 0.8mm
Reles pequeño | 1mm | 0.8mm
Reles grandes |  | 
Conectores |  | 1mm







# Exportar el PCB


Para exportar hay que tener en cuenta el diseño del PCB, si se ha creado el PCB en la capa superior (no recomendable) sera necesario exportarlo en modo espejo, en nuestro caso se va a partir de que se ha diseñado el conexionado en la capa inferior y en la capa superior solo esta la serigrafía de los componentes, ahorrando que sea necesario exportarlo en modo espejo.

La exportación seria en formato PDF y las capas que habría que exportar son las siguientes:


|Capas|
|----|
|Capa inferior|
|Bordes de placa|
|Multi-Layer|
|Orificio|


Como recomendación esta en usar como motor el ordenador local, haciendo que tarde bastante menos tiempo que si se genera el PDF por el servidor.

A continuación podemos ver una imagen de la ventana de exportación:

![easy](/images/2019/export_easueda.png){:height="auto" width="100%"}



# Impresión del PCB



Para imprimir en papel fotográfico es recomendable seguir estas recomendaciones:


- Realizar un limpiado de los cabezales de la impresora, ya que se necesita que la imagen sea precisa.
- Configurar la impresora para que use papel A6, con el objetivo de poder aprovechar ese papel para otras impresiones.
- Configurar el papel como grueso, para que caliente mas el papel y se obtenga mejor impresión.
- Configurar la resolución en alta (1200 Res)






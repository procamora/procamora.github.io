---
title: Flashear Nexus 9
description: Vamos a explicar el proceso para flashear la Nexus 9 LTE con distintas ROMs mediante adb sideload. Este es un proceso bastante mas simple y rápido que los que se realizaban antiguamente. Se puede realizar en cualquier dispositivo. Este procedimiento ha sido probado con las ROMs de LineageOS y SlimRoms.
date: 2019-10-03
image: "covers/android.png"
slug: "flashear-nexus-9"
tags:
  - nexus9
  - lineageos
  - slimroms
  - twrp
  - adb
  - sideload
categories:
  - Android
---

Status: published


Vamos a explicar el proceso para flashear la Nexus 9 LTE con distintas ROMs mediante `adb sideload`. Este es un proceso bastante mas simple y rápido que los que se realizaban antiguamente. Se puede realizar en cualquier dispositivo.

Este procedimiento ha sido probado con las ROMs de LineageOS y SlimRoms.









# Requisitos básicos

1. Tener instalado `adb` y `fastboot`.
1. Tener habilitado el USB debugging en el dispositivo.

> Verificar que se tiene permiso para ejecutar `adb` con el usuario. En caso de no tener permiso realizarlo con root.








# Desbloquear el bootloader


1. Si esta activado el bloqueo OEM hay que desactivarlo en las opciones de desarrollo.
1. Reiniciamos el dispositivo en modo fastboot:

	```bash
	adb reboot bootloader
	```

	> También se puede hacer presionando las teclas: **Bajar volumen** y **Power** con el dispositivo apagado hasta que aparezca el gestor de arranque. Después seleccionar _FASTBOOT_ y pulsar **Power**.

1. Verificar que el dispositivo esta en modo _FASTBOOT_ con:

	```bash
	fastboot devices
	```

	```
	HT51EWV00595    fastboot
	```

1. Si el dispositivo esta bloqueado con OEM hay que desbloquearlo con:

	```bash
	fastboot oem unlock
	```

	```
	(bootloader) ability is 1
	(bootloader) Device stete is unlock already
	OKAY [  0.142s]
	Finished. Total time: 0.142s
	```

	> Este comando reiniciara el dispositivo automáticamente.








# Instalar un recovery personalizado usando fastboot

1. Descargar un recovery personalizado, como por ejemplo [TWRP][twrp]. Este tendrá un formato similar a _twrp-x.x.x-x-flounder.img_.

	> Importante, descargar el recovery des dispositivo que vas a usar puedes buscarlo en https://twrp.me/Devices/

1. Reiniciar el dispositivo en modo _FASTBOOT_, para ello es necesario que el dispositivo este encendido. Este paso se puede saltar si ya se tenia desbloqueado el OEM, ya que el dispositivo no se habrá reiniciado y seguirá en modo _FASTBOOT_.

	```bash
	adb reboot bootloader
	```

1. Verificar que el dispositivo esta en modo _FASTBOOT_ con:

	```bash
	fastboot devices
	```

	```
	HT51EWV00595    fastboot
	```

1. Flashear el dispositivo con la imagen previamente descargada:


	```bash
	fastboot flash recovery <recovery_filename>.img
	```


	```
	Sending 'recovery' (13254 KB)                      OKAY [  0.761s]
	Writing 'recovery'                                 (bootloader) Device State : Unlocked
	OKAY [  1.034s]
	Finished. Total time: 1.800s
	```


1. Reiniciar el dispositivo en modo recovery, esto se puede realizar manualmente usando las teclas de _Volumen_ y _Power_ o con el comando:

	```bash
	fastboot boot <recovery_filename>.img
	```

	```
	Downloading 'boot.img'                             OKAY [  0.740s]
	booting                                            OKAY [  0.174s]
	Finished. Total time: 0.919s
	```



# Instalar ROM desde el recovery

1. Descargar la ROM deseada, en mi caso ha sido [SlimRoms][slimroms_nexus9].

1. Descargar las Google Apps, están disponibles en [OpenGApps][gapps]. Para la Nexus 9 hay que seleccionar como plataforma ARM64. Con la *nano* es suficiente.

1. Una vez descargados los ficheros que vamos a utilizar, tenemos que estar en el modo Recovery con TWRP.

1. Vamos al menú de **Wipe**
   - Seleccionamos **Format Data** y escribimos _yes_. Este proceso elimina la encriptación del disco y borra los datos de la memoria interna.
   - Volvemos al menú de **Wipe** y seleccionamos **Advanced Wipe**. Aquí seleccionamos _Cache_ y _System_ para hacer un wipe de estas particiones 


1. Finalmente solo queda instalar la ROM y las GApps, para hacer esto vamos a **Advanced** y después a **ADB Sideload**, hacemos swipe para iniciar el sideload, después de cada instalación es necesario volver a iniciarlo.
	- Instalamos la ROM 
	- Instalamos las GApps

	```bash
	adb sideload rom.zip
	adb sideload gapps.zip
	```



1. **IMPORTANTE:** [Instalar FED-Patcher v7 (ForceEncrypt Disable Patcher)][FED], solo en la Nexus 9 con el objetivo de que el disco no se cifre, ya que reduce el rendimiento y se nota bastante. Podemos descargarlo tanto del foro xda, donde su creador lo ha publicado como desde [aquí][fedv7].


	```bash
	adb sideload fed_patcher_v7-signed.zip
	```



1. Una vez instalado todo lo necesario reiniciar el dispositivo y esperar a que arranque con normalidad, puede llegar a tardar mas de 10 minutos.

	```bash
	adb reboot
	```


Como fuente para la realización de este manual se ha usado: [0][Fuente0]

[twrp]: https://dl.twrp.me/flounder/

[slimroms_nexus9]: https://slimroms.org/#/device/flounder_lte
[gapps]: https://opengapps.org/?api=7.1&variant=nano
[FED]: https://forum.xda-developers.com/nexus-9/development/fix-fed-patcher-forceencrypt-disable-t3200168
[fedv7]: /descargas/fed_patcher_v7-signed.zip

[Fuente0]: https://wiki.lineageos.org/devices/flounder_lte/install
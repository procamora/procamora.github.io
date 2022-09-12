#!/bin/bash
# https://stackoverflow.com/questions/9853325/how-to-convert-a-svg-to-a-png-with-image-magick

DENSITY=250 

#python3 delete_watermark.py

#convert -density $DENSITY DC_Parser.svg DC_Parser.png
#convert -density $DENSITY DC_Tables.svg DC_Tables.png
#convert -density $DENSITY Docker-Compose.svg Docker-Compose.png



inkscape --file=2019/burn_bootloader.svg --export-area-drawing --without-gui --export-pdf=2019/burn_bootloader.pdf
#inkscape --file=2019/proxmox.svg --export-area-drawing --without-gui --export-png=2019/proxmox.png
 
convert -density $DENSITY 2019/Escenario.svg 2019/Escenario.png

inkscape --file=pdf.svg --export-area-drawing --without-gui --export-png=pdf.png

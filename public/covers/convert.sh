#!/bin/bash
# https://stackoverflow.com/questions/9853325/how-to-convert-a-svg-to-a-png-with-image-magick

# pip install optimize-images
optimize-images --no-recursion ./

#DENSITY=250 
#convert -density $DENSITY DC_Parser.svg DC_Parser.png
#convert -density $DENSITY DC_Tables.svg DC_Tables.png
#convert -density $DENSITY Docker-Compose.svg Docker-Compose.png

inkscape -z --export-filename windows2.png -h 40 windows.svg

#inkscape --file=Metodologia.svg --export-area-drawing --without-gui --export-pdf=Metodologia.pdf

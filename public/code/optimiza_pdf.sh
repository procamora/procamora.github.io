#!/bin/bash
#Script para optimizar pdf se para como argumento el pdf
# para ejecutarlo sobre un directorio find . -type f -name "*.pdf" -exec ./optimiza_pdf.sh {} \;

TEMP="temporal.pdf"

echo "$1"
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$TEMP" "$1"
mv "$TEMP" "$1"
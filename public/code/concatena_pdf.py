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

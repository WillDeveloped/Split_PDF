#This program walks a directory, takes all the PDF's, splits what ever page
#you want out, and saves it as it's own file. If the directory contains
#files other than PDF's, a try/exception would need to be inserted. 

import PyPDF2 
import os
import os.path
from PyPDF2.pdf import PdfFileReader, PdfFileWriter

DIR_TO_WALK = ""    #Insert directory to walk here. For instance, if I wanted to walk all files in directory "Documents",
                    #I would set this to: "C:\Users\william\Documents"

PAGE_TO_SPLIT = 0    #Change this number to the page you want extracted from the PDF

for root, dirs, files in os.walk(DIR_TO_WALK):
    for name in files:      
        with open(DIR_TO_WALK + "\\" + name, 'rb') as infile:
            reader = PdfFileReader(infile, strict = False)
            writer = PdfFileWriter()
            writer.addPage(reader.getPage(PAGE_TO_SPLIT))
    
            with open(name, 'wb') as outfile: #File will be saved as original file name
                writer.write(outfile)

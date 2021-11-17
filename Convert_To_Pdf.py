
#Para baixar o módulo, utilize do parâmetro "pip install tabula-py"

#Importando o módulo Tabula-py 

import tabula

#Lê o arquivo em PDF

Pdf_File = tabula.read_pdf("arqivo.pdf", pages = 'all') [0]

#Converter o PDF em Excel

tabula.convert_into("arquivo.pdf", "arquivo.csv", output_format = "csv", pages = 'all')

print(Pdf_File)


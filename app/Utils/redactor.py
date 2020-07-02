import re
import sys
import os
import xml.etree.ElementTree as ET
from shutil import make_archive
from datetime import datetime

def redactor(aluno, pathXML, pathCopia, pathNovo):
    tree = ET.parse(pathXML)

    #Textboxes X e X
    textboxes = tree.getroot()[0][0][1][2][0][0][0][7][0][0][2][0][0]
    for i in range(1,6):
        textboxes[i][1].text = textboxes[i][1].text.replace("(NOME)", aluno.nome.upper()).replace("(CURSO)", aluno.curso.upper()).replace("(SEMESTRE)", aluno.getSemestre().upper()).replace("(ANO)", str(aluno.data_inscricao.year)).replace("(ANOC)", str(aluno.data_certificado.year)).replace("(MES)", aluno.getMes().upper()).replace("(DIA)", str(aluno.data_certificado.day))

    tree.write(pathCopia + "/word/document.xml")

    make_archive(pathNovo, 'zip', pathCopia)
    os.rename(pathNovo + ".zip", pathNovo)

def teste():
    pathXML = os.path.dirname(__file__) + "/base/alunoXML/word/document.xml"
    pathCopia = os.path.dirname(__file__) + "/certificados/baseXML" 
    pathNovo = os.path.dirname(__file__) + "/certificados/teste.docx"

    tree = ET.parse(pathXML)
    
    #Textboxes X e X
    textboxes = tree.getroot()[0][0][1][2][0][0][0][7][0][0][2][0][0]
    for i in range(1,6):
        print(textboxes[i][1].text)
        #i.text = i.text.replace("(NOME)", "Vinícius Aiala".upper()).replace("(CURSO)", "Python".upper()).replace("(SEMESTRE)", "segundo semestre".upper()).replace("(ANO)", "2020").replace("(MES)", "maio".upper()).replace("(DIA)", "20")

    #tree.write(pathCopia + "/content.xml")

    #make_archive(pathNovo, 'zip', pathCopia)
    #os.rename(pathNovo + ".zip", pathNovo)

if __name__ == "__main__":
    teste()
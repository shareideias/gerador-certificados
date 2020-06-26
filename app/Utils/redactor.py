import re
import sys
import os
import xml.etree.ElementTree as ET
from shutil import make_archive
from datetime import datetime

def redactor(aluno, pathXML, pathCopia, pathNovo):
    tree = ET.parse(pathXML)

    #Textboxes X e X
    textboxes = tree.getroot()[3][0][2]
    for j in range(2):
        for i in textboxes[j][0][0]:
            i.text = i.text.replace("(NOME)", aluno.nome.upper()).replace("(CURSO)", aluno.curso.upper()).replace("(SEMESTRE)", aluno.getSemestre().upper()).replace("(ANO)", str(aluno.data_inscricao.year)).replace("(ANOC)", str(aluno.data_certificado.year)).replace("(MES)", aluno.getMes().upper()).replace("(DIA)", str(aluno.data_certificado.day))

    tree.write(pathCopia + "/content.xml")

    make_archive(pathNovo, 'zip', pathCopia)
    os.rename(pathNovo + ".zip", pathNovo)

def teste():
    pathXML = os.path.dirname(__file__) + "/base/alunoXML/content.xml"
    pathCopia = os.path.dirname(__file__) + "/certificados/baseXML" 
    pathNovo = os.path.dirname(__file__) + "/certificados/teste.odt"

    tree = ET.parse(pathXML)
    #Textboxes X e X
    textboxes = tree.getroot()[3][0][2]
    for j in range(2):
        for i in textboxes[j][0][0]:
            print(i.text)
            #i.text = i.text.replace("(NOME)", "Vinícius Aiala".upper()).replace("(CURSO)", "Python".upper()).replace("(SEMESTRE)", "segundo semestre".upper()).replace("(ANO)", "2020").replace("(MES)", "maio".upper()).replace("(DIA)", "20")

    #tree.write(pathCopia + "/content.xml")

    #make_archive(pathNovo, 'zip', pathCopia)
    #os.rename(pathNovo + ".zip", pathNovo)

if __name__ == "__main__":
    teste()
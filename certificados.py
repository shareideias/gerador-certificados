import os
import sys

import postgresql

from mailmerge import MailMerge
from shutil import make_archive
from shutil import rmtree

from docx2pdf import convert
from datetime import date

from Participante import Participante

def main():
    try:
        id_curso = 7 #sys.argv[1]
        n_horas = 30 #sys.argv[2]
    except:
        print("Curso ou/e número de horas não especificado")
        return

    #Conexão com o BD 
    try:
        db = postgresql.open('pq://postgres:4223@localhost:5432/shareideias')
        sql = "SELECT par.nome, par.curso1_id AS curso_id, cur.nome, par.data_inscricao_c1 AS data_inscricao FROM sisins_participante AS par JOIN sisins_curso AS cur ON par.curso1_id = cur.id  WHERE (par.curso1_id = {0} AND par.resultado_c1 = 1) UNION SELECT par.nome, par.curso2_id AS curso_id, cur.nome, par.data_inscricao_c2 AS data_inscricao FROM sisins_participante AS par JOIN sisins_curso AS cur ON par.curso2_id = cur.id  WHERE (par.curso2_id = {0} AND par.resultado_c2 = 1)".format(id_curso)
        query = db.prepare(sql)
    except:
        print("Erro na conexão com o BD:", sys.exc_info())
        return

    certPath = os.path.dirname(__file__) + "/certificados"
    zipPath = os.path.dirname(__file__) + '/Certificados'
    pathBase = os.path.dirname(__file__) + "/base/aluno.docx"

    #Tenta realizar
    try:
        #Cria o diretório dos certificados
        rmtree(certPath, ignore_errors=True)
        os.mkdir(certPath)

        #Repete para todos os alunos
        for row in query:
            aluno = Participante(row)
            #Gera o certificado de cada aluno
            geraCertificado(aluno, pathBase, n_horas)

        #Zipa todos
        make_archive(zipPath, 'zip', certPath)
    except:
        print("Erro na geração de arquivos:", repr(sys.exc_info()[0]), repr(sys.exc_info()[1]), sys.exc_info()[2].print_exc())
        return
    finally:
        #Exclui os certificados
        rmtree(certPath, ignore_errors=True)
        pass

# Deve pegar editar o modelo em memória e colocar no padrão, zipar e excluir o xml
def geraCertificado(aluno, pathBase, n_horas):
    #DOCX
    pathNovo = os.path.dirname(__file__) + "/certificados/{0}.docx".format(aluno.nome)
    template = pathBase
    document = MailMerge(template)
    
    document.merge(
        DIAMESANO = date.today().strftime("%d/%m/%Y"),
        HORAS = str(n_horas),
        ANO = str(aluno.data_inscricao.year),
        NOME = aluno.nome.upper(),
        CURSO = aluno.curso.upper(),
        SEMESTRE = aluno.getSemestre().upper()
    )

    document.write(pathNovo)

    #PDF
    convert(pathNovo)
    os.remove(pathNovo)

if __name__ == "__main__":
    main()
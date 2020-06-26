class Participante:
    def __init__(self, info):
        self.nome = info[0]
        self.curso = info[2]
        self.data_inscricao = info[3]
        self.data_certificado = info[4]
    
    def __repr__(self):
        return "nome = {0}, curso = {1}, data_inscricao = {2}, data_certificado = {3}".format(self.nome, self.curso, self.data_inscricao, self.data_certificado)

    def getSemestre(self):
        return "PRIMEIRO SEMESTRE" if self.data_inscricao.month < 7 else "SEGUNDO SEMESTRE"
        
    def getMes(self):
        switcher = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }
        return switcher[self.data_certificado.month]
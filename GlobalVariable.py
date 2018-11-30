class GlobalVariable():
    def __init__(self,nome,score,fim):
        self.nome = nome
        self.score = score
        self.fim = fim

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setScore(self,score):
        self.score = score

    def getScore(self):
        return self.score

    def setFim(self,fim):
        self.fim = fim

    def getFim(self):
        return self.fim
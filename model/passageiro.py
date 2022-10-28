
class Passageiro():
    
    def __init__(self, aluno, cidadeOrigem, cidadeDestino):
        self.aluno = aluno
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return 'Aluno {}\nCidade Origem {} Cidade Destino {}\n '.format(self.aluno, self.cidadeOrigem, self.cidadeDestino)
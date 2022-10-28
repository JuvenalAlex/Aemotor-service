class Uf():
    
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla

    def __repr__(self):
        return 'Nome {} Sigla {}\n'.format(self.nome, self.sigla)
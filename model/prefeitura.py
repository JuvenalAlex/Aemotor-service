class Prefeitura():

    def __init__(self, secretarios, email, telefone, nomePrefeito):
        self.secretarios = secretarios
        self.email = email
        self.telefone = telefone
        self.nomePrefeito = nomePrefeito

    def __repr__(self):
        return '<Secretarios: {} Email: {} Telefone: {} Nome do Prefeito: {}'.format(self.secretarios, self.email, self.telefone, self.nomePrefeito)
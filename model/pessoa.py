from helpers.database import db
class Pessoa(db.Model):
    __tablename__ = 'tb_pessoa'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_endereco.id'))
    
    child = db.relationship("Aluno", uselist=False)
    child2 = db.relationship("Prefeito", uselist=False)
    child3 = db.relationship("Funcionario", uselist=False)
    
    endereco = db.relationship("Endereco")
    
    def __init__(self, nome, nascimento, email, telefone,endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return 'Nome: {} Data de Nascimento: {} Email: {} Telefone: {}\n'.format(self.nome, self.nascimento, self.email, self.telefone)
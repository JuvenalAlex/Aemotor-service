from helpers.database import db
class Pessoa(db.Model):
    __tablename__ = 'tb_pessoa'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_endereco.id'))
    
    childaluno_ = db.relationship("Aluno", uselist=False)
    childprefeito_ = db.relationship("Prefeito", uselist=False)
    childfuncionario_ = db.relationship("Funcionario", uselist=False)
    childendereco_ = db.relationship("Endereco", uselist=False)
    childgestor_ = db.relationship("GestorApp", uselist=False)
    
    
    def __init__(self, nome, nascimento, email, telefone,endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return 'Nome: {} Data de Nascimento: {} Email: {} Telefone: {}\n'.format(self.nome, self.nascimento, self.email, self.telefone)
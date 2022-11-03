from helpers.database import db
from model.motorista import Motorista
class Funcionario(db.Model):
    __tablename__ = "tb_funcionario"
    
    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String(90), nullable=False)
    cargo = db.Column(db.String(30), nullable=False)
    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_id = db.Column(db.Integer, db.ForeignKey('Funcionario.id'), nullable=False)
   
    motorista = db.relationship("Motorista", uselist=False)
    pessoa = db.relationship("Pessoa")
    
    def __init__(self, prefeitura, cargo, pessoa):
        self.prefeitura = prefeitura
        self.cargo = cargo
        self.pessoa = pessoa

    def __repr__(self):
        return '\nPrefeitura {}\n Cargo {}\n'.format(self.prefeitura, self.cargo)

    
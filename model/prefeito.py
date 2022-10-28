from model.pessoa import Pessoa
from helpers.database import db

class Prefeito(Pessoa,db.Model):
    
    __tablename__ = 'tb_prefeito'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return 'Prefeito:{}\n '.format(self.pessoa)

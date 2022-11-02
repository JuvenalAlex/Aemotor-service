from model.funcionario import Funcionario
from helpers.database import db

class Motorista(Funcionario,db.Model):
    __tablename__ = 'tb_motorista'

    id = db.Column(db.Integer, primary_key=True)
    rotas = db.Column(db.String(80), nullable=False)
    funcionario_id = db.Column(db.Integer, db.ForeignKey("tb_funcionario.id"))
    
    funcionario = db.relationship("Funcionario")
    veiculo_child = db.Relationship('Veiculo',uselist=False)
    
    def __init__(self, rotas,funcionario):
        self.funcionario = funcionario
        self.rotas = rotas

    def __repr__(self):
        return 'Rotas {}\n '.format(self.rotas, self.funcionario)
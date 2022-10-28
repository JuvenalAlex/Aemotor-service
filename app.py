from model.aluno import Aluno
from model.cidade import Cidade
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.gestorApp import GestorApp
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import Uf
from model.veiculo import Veiculo



pessoa = Pessoa("Juvenal", "28/11/2002", "email@juvenal", "93455-5452")
print(pessoa)

aluno = Aluno("Deris", "17/11/2001", "Deris@email", "934345-3321", "IFPB", "TSI", "2020201232")
print(aluno)

cidade = Cidade("Guarabira", "GBA")
print(cidade)

endereco = Endereco("58340-000", "177", "Casa", "Próximo ao Afonso Júnior", "Rua Juscelino Kubistchek")
print(endereco)

prefeitura = Prefeitura("Marcelo", "email@Marcelo", "1587-5152", "Marcelo")
print(prefeitura)

funcionario = Funcionario(prefeitura, "Menino da Informática")
print(funcionario)

veiculo = Veiculo("Guarabira", "44", "Ônibus", "GOS-7329")
print(veiculo)


gestor = GestorApp(pessoa)
print(gestor)

instituto = InstituicaoDeEnsino("IFPB", "Rua Professor Carlos Leonardo Arcoverde", "98195-6465")
print(instituto)

motorista = Motorista("A ser determinado",funcionario)
print(motorista)


passageiro = Passageiro(aluno, "Sapé", "Guarabira")
print(passageiro)

pessoa2 = Pessoa("Sidney","22/12/2002","sidney@email","92234-2343")
prefeito = Prefeito(pessoa2)
print (prefeito)

rota = Rota("Guarabira", "44", "Sapé", "ônibus", "Jean", "06:00h", "07:00h")
print(rota)

uf = Uf("Paraíba", "PB")
print(uf)
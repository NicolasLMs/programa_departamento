from utils import *


nome_departamento = input('Qual será o nome do departamento? ')
departamento = Departamento(nome_departamento)
qtd_funcionario = int(input('Quantos funcionários serão adicionados? '))
limpar_terminal()

for i in range(qtd_funcionario):
    nome, idade, salario = solicitar_dados_funcionario(i+1)
    funcionario = Funcionario(nome, idade, salario)
    departamento.adiciona_funcionario(funcionario)
    limpar_terminal()

departamento.soma_salarios_anuais()
departamento.listar_funcionarios()
import os

def solicitar_dados_funcionario(f):
    nome = input(f"Nome do {f}° funcionário: ")
    idade = int(input(f"Idade do {f}° funcionário: "))
    salario = float(input(f"Salário do {f}° funcionário: "))
    return nome, idade, salario

def limpar_terminal():
    os.system('cls')
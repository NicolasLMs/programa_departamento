import os

def limpar_terminal():
    os.system('cls')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        if self.idade < 18:
            self.set_idade()

    def set_idade(self):
        while self.idade < 18:
            print(f"Idade inválida para {self.nome}.")
            try:
                idade_nova = int(input(f"Digite uma nova idade para {self.nome} (maior ou igual a 18): "))
                limpar_terminal()
                if idade_nova >= 18:
                    self.idade = idade_nova
                else:
                    print("Idade deve ser maior ou igual a 18.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.__salario = salario

    @property
    def get_salario(self):
        return self.__salario

    @get_salario.setter
    def set_salario(self, novo):
        self.__salario = novo

    def calcula_salario_anual(self):
        return self.__salario * 12

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = []

    def soma_salarios_anuais(self):
        total = 0
        for funcionario in self.lista_funcionarios:
            total += funcionario.calcula_salario_anual()
        print(f"Total dos salários anuais do departamento de {self.nome} foi: R$ {total:.2f}")

    def adiciona_funcionario(self, funcionario):
        if funcionario not in self.lista_funcionarios:
            self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\nLista de funcionários do departamento de {self.nome}:")
        for funcionario in self.lista_funcionarios:
            print('-' * 30)
            print(f"Funcionário: {funcionario.nome}, Salário anual: R$ {funcionario.calcula_salario_anual():.2f}")

def solicitar_dados_funcionario():
    nome = input("Nome do funcionário: ")
    idade = int(input("Idade do funcionário: "))
    salario = float(input("Salário do funcionário: "))
    return nome, idade, salario

def main():
    nome_departamento = input('Qual será o nome do departamento? ')
    departamento = Departamento(nome_departamento)
    qtd_funcionario = int(input('Quantos funcionários serão adicionados? '))

    for _ in range(qtd_funcionario):
        nome, idade, salario = solicitar_dados_funcionario()
        funcionario = Funcionario(nome, idade, salario)
        departamento.adiciona_funcionario(funcionario)
        limpar_terminal()

    departamento.soma_salarios_anuais()
    departamento.listar_funcionarios()

if __name__ == "__main__":
    main()
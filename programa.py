import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    def __init__(self):
        self.lista_funcionarios = []

    def soma_salarios_anuais(self):
        total = 0
        for funcionario in self.lista_funcionarios:
            total += funcionario.calcula_salario_anual()
        print(f"Total dos salários anuais do departamento: R$ {total:.2f}")

    def adiciona_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print("\nLista de funcionários do departamento:")
        for funcionario in self.lista_funcionarios:
            print(f"Funcionário: {funcionario.nome}, Salário anual: R$ {funcionario.calcula_salario_anual():.2f}")

pessoa1 = Pessoa("Alice", 16)
pessoa2 = Pessoa("Bob", 25)
pessoa3 = Pessoa("Charlie", 17)

funcionario01 = Funcionario(pessoa1.nome, pessoa1.idade, 1700.00)
funcionario02 = Funcionario(pessoa2.nome, pessoa2.idade, 3000.00)
funcionario03 = Funcionario(pessoa3.nome, pessoa3.idade, 2200.00)

departamento = Departamento()
departamento.adiciona_funcionario(funcionario01)
departamento.adiciona_funcionario(funcionario02)
departamento.adiciona_funcionario(funcionario03)

departamento.soma_salarios_anuais()
departamento.listar_funcionarios()
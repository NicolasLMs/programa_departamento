class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)

    def set_idade(self,idade):
        while idade < 18:
            print(f'Idade invalida para {self.nome}, restrição para menores de 18 anos')
            idade = int(input('digite uma nova idade: '))
        self.idade = idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo):
        while novo < 0:
            print(f'Salário de {self.nome} definido com um valor nulo')
            novo = float(input('digite um novo valor para salário: '))
        self.__salario = novo

    def calcula_salario_anual(self):
        return self.salario * 12

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

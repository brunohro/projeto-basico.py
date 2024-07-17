from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario, cargo):
        super().__init__(nome, idade)
        self.salario = salario
        self.cargo = cargo 

    def mostrar_detalhes(self):
        detalhes_pessoa = super().mostrar_pessoa()
        return f"{detalhes_pessoa}, Salário: {self.salario}, Cargo: {self.cargo}"
class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def mostrar_pessoa(self):
        return f"Nome: {self.nome}, idade: {self.idade}"
    
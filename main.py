
from funcionario import Funcionario
from pessoa import Pessoa

pessoa = Pessoa("João", 30)
funcionario = Funcionario("Maria", 28, 5000, "Engenheira de Software")

print(pessoa.mostrar_pessoa())
print(funcionario.mostrar_detalhes())

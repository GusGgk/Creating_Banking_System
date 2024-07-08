nome ="Gustavo"
idade = 18
profissao = "Programador"
lingaugem = "Python"

saldo = 45.435
#criando um dicionario
dados = {"nome": "Gustavo", "idade": 28,}


# na interpolação %
print("Nome: %s Idade: %d" % (nome, idade))

# na interpolação format

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {0} Idade: {1} Nome = {0} {0}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))


#f string
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")


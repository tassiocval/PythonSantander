nome = "Tassio"
idade = 30
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"name": "Tassio", "idade": 20}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {0} Idade: {1}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome,  idade=idade))
print("Nome: {name} Idade: {age}".format(name=nome,  age=idade))
print("Nome: {name} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")

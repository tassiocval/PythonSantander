# AND - para ser True tudo deve ser True
# OR - para ser True apenas um tem que ser True

saldo = 1080
saque = 250
limite = 280
conta_especial = True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
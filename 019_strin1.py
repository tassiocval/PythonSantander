curso = "TassiO"

print(curso.center(10, "-"))
print(".".join(curso))
print(curso.lower())
print(curso.upper())
print(curso.count(curso))

tetxo = " Ola mundo"

print(tetxo)
print(tetxo.strip() + ".")
print(tetxo.rstrip() + ".")
print(tetxo.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14,"#"))
print("-".join(menu))

for i in menu:
    print(i, end=" ")
senha_correta = "admin"
senha = input("Digite sua senha: ")

while True:
    senha = input("Digite sua senha: ")

    if senha == senha_correta:
        print("Login Válidado com sucesso!")
        break
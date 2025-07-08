texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo usando a funcao um interavel    
for letra in texto:
    if letra.upper() in VOGAIS:
        
        
        print(letra, end=" ")


else:
    print()
   

# Exemplo usando a funcao built-in range
for numero in range(0, 51, 5):
    print(f"{numero}")
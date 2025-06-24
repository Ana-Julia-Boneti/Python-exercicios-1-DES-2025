#Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
#Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)

numeros = []

for i in range(0, 3, 1):
    numeros.sort(int(input("Digite um numero")))

numeros.sort()
print(numeros)

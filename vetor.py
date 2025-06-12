import random

frutas = {"maçã", "Banana", "Laranja", "Uva", "Manga"}
print ("Lista de Frutas:")
for i in range (len(frutas)):
    print(f"{i + 1} - {frutas[i]}")
posicao_sorteada = random.randint(1, 5)
palpite = input("Qual fruta você acha que esta na posição sorteada?")
fruta_certa = frutas[posicao_sorteada - 1]
if palpite.capitalize() == fruta_certa:
    print("Parabéns! Você acertou!")
    print(f"a fruta na posição {posicao_sorteada} era realmente {fruta_certa}.")
else:
    print("Que pena! Você errou.")
    print(f"A fruta na posição {posicao_sorteada} era {fruta_certa}.")
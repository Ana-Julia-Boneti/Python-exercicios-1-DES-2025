# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)
meta_01 = int(input("digite a avaliação 01"))
meta_02 = int(input("digite a avaliação 02"))
meta_03 = int(input("digite a avaliação 03"))

if meta_01+meta_02+meta_03 <=7:
    print ("aprovado")
elif  meta_01+meta_02+meta_03 >=5 <7:
    print ("em treinamento")
elif  meta_01+meta_02+meta_03 :
    print("reprovado")
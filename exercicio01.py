# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.
curso01 = int(input(" digite qual foi a avaliação do curso01"))
curso02 = int(input("digite qual foi a avaliação do curso02"))

if curso01>curso02:
    print("curso01 teve mais avaliações")
else:
    print("curso02 teve menos avaliações")
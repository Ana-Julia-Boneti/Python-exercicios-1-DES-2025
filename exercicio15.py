#Peça a idade do usuário e diga se ele pode se cadastrar em um site:

#Permitido: 13 anos ou mais
idade = int(input("digite a sua idade"))
if idade >= 13:
    print("essa idade é permitida nesse site")
else:
    print("sua idade não é permitida")
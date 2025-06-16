#Loja oferece os seguintes descontos:

#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto

valor = int(input("digite o valor  compra"))
if  valor <= 500:
    desconto = ("voce ganhou 10% de desconto")
elif valor >= 300:
    desconto =  ("voce ganhou 5% de desconto")
else:
    print (f"o valor de {desconto} é a % {valor:.2f}")
# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00
distancia = int(input("digite o numero da distancia em km"))

if distancia <= 50 :
    frete = 5,00
elif distancia <= 150:
    frete = 15,00
else:
    frete = 25,00
    print (f"o valor do frete para {distancia} km é R$ { frete:.2f}")


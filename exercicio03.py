# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.
umidade_local =  int(input("digite o valor da umidade"))

if umidade_local < 70:
    print ("a umidade está correta")
else:
    print ("a umidade está muito baixa")

# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

internet_mensal = int(input("digite o valor de internet consumidos no mes"))

if internet_mensal >100 :
    print ("você ultrapassou o limite de internet")
else:
    print ("você está dentro do limite de GB")
# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.

acesso_permitido = int(input("digite quantos acessos a plataforma teve "))

if acesso_permitido == 9:
    print ("horario de funcionamento")
elif acesso_permitido == 21:
    print ("horario de funcionamento")  
else:
    print ("horario não esta disponivel")                

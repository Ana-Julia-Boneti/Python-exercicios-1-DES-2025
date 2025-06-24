#Simule um login com nome de usuário "admin" e senha "1234".
#Caso os dados estejam corretos, exiba "Acesso concedido", senão "Acesso negado".

usuario = input("digite seu nome de usuario")
senha = input("digite sua senha")

if usuario == "admin" and senha == "1234":
    print ("acesso permitido")
else:
    print("acesso negado")

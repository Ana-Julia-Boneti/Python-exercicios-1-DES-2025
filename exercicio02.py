#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

projeto_01 = int(input("primeiro projeto"))
projeto_02 = int(input("segundo projeto"))
projeto_03 = int(input("terceiro projeto"))

if projeto_01 < 0 or projeto_02 < 0 or projeto_03 < 0:
    print("erro, numero negativo")
else:
    soma = projeto_01 + projeto_02 + projeto_03
    print("dias totais de projeto: {soma} dias")
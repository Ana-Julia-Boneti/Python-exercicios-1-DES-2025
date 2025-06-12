alunos = {"Alice", "Bruno", "Carla"}
dias = {"seg", "Ter", "Qua", "Qui"}
reservas = [["ausente" for _ in dias]for _ in alunos]]
print("Preencha com 'S' para presença e 'x' para ausência.")
for i, Aluno in enumerate(alunos):
    print(f"\nAluno: {Aluno}")
    for J, dia in enumerate(dias):
        entrada = input(f"  {dia}: ")
        if entrada.upper() == 's':
            reservas[i][J] = "presente"

print("\n tabela de reservas:")
print(f"{'Aluno':<10} {''.join([{f'd:<10}' for d in dias])}")
for i, Aluno in enumerate(alunos):
    print(f"{Aluno:<10} {''.join([f'{res:<10}'])}")

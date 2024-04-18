aluno = {}
aluno["Nome"] = str(input("Digite o nome do(a) aluno(a): "))
aluno["Média"] = float(input(f"Digite a média de {aluno["Nome"]}: "))
if aluno["Média"] >= 7:
    aluno["Situação"] = "\033[32mAprovado(a)!\033[m]"
elif 7 > aluno["Média"] >= 5:
    aluno["Situação"] = "\033[33mRecuperação...\033[m"
else:
    aluno["Situação"] = "\033[31mReprovado(a)!\033[m]"
print("-="*20)
for k, v in aluno.items():
    print(f"{k} ====> {v}")
    print("-="*20)

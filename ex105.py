def notas(*n, sit=False):
    """A função notas pode receber várias notas e retorna a quantidade de notas, a maior nota,
    a menor nota, a média da turma e a situação(opcional).
    param n ---> Notas de alunos para serem analisadas.
    param sit ---> Situação da turma(opcional)."""
    turma = dict()
    s = 0
    turma["Total de notas"] = len(n)
    turma["Maior nota"] = max(n)
    turma["Menor nota"] = min(n)
    for v in n:
        s += v
    media = s / len(n)    
    turma["Média da turma"] = media    
    if sit:
        if media >= 10:
            turma["Situação"] = "PERFEITA!"
        elif 10 > media >= 7:
            turma["Situação"] = "BOA."
        elif 7 > media >= 5:
            turma["Situação"] = "RAZOÁVEL."
        elif 5 > media >= 3:
            turma["Situação"] = "RUIM!"
        else:
            turma["Situação"] = "PÉSSIMA!!!"         
    return turma


# Programa Principal
resp = notas(10, 10, 10, 10, sit = True)
print(resp)    
#help(notas)

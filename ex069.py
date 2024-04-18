resposta = maiores = homens = meninas = 0
cont = 1
print("-=" * 16)
print("      ANALISADOR DE DADOS")
print("-=" * 16)
while True:
    idade = int(input(f"Quantos anos tem a {cont}ª pessoa?"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input(f"Qual o sexo da {cont}ª pessoa?[M/F]:")).upper().strip()
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Você deseja continuar?[S/N]:")).upper().strip()[0]
    if resposta == "S":
        cont += 1
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        meninas += 1
    if resposta == "N":
        break
print(f"""---------------------------------------------
FORAM CADASTRADO(S) {cont} USUÁRIO(S)
---------------------------------------------
{maiores} USUÁRIO(S) MAIOR(ES) DE 18 ANOS CADASTRADO(S)
{homens} USUÁRIO(S) DO SEXO MASCULINO CADASTRADO(S)
{meninas} USUÁRIO(S) DO SEXO FEMININO E MENOR(ES) DE 20 ANOS CADASTRADO(S)
---------------------------------------------
FIM DE ANÁLISE
---------------------------------------------
""")

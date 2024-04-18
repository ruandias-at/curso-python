ano = int(input("Digite seu ano de nascimento:"))

if ano == 2006:
    print("É a hora de se alistar!")
elif ano < 2006:
    print("""Já passou do tempo de seu alistamento!
Você está {} ano(s) atrasado!""".format((ano - 2006) * -1))
else:
    print("""Ainda vai chegar sua hora de se alistar. 
Falta(m) {} ano(s) para seu alistamento.""".format(ano - 2006))



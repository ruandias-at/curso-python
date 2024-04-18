aberto = []
fechado = []
expressao = list(input("Digite uma expressão: "))
for simb in expressao:
    if simb == "(":
        aberto.append("(")
    elif simb == ")":
        fechado.append(")")            
if len(aberto) == len(fechado):
    print("\033[32mSua expressão é válida!\033[m")
else:
    print("\033[31mSua expressão está errada!\033[m")    

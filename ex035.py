print("-=" * 20)
print("            \033[0;31m DESAFIO MASTER \033[m")
print("-=" * 20)

a = float(input("Comprimento lado A:"))
b = float(input("Comprimento lado B:"))
c = float(input("Comprimento lado C:"))

if a + b > c and a + c > b and c + b > a:
    print("É possível formar um triângulo a partir destes comprimentos.")
else:
    print("Não é possível formar um triângulo com essas medidas.")

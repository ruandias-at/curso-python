print("-=" * 15)
print(" \033[31mSEQUÊNCIA DE FIBONACCI v1.0\033[m")
print("-=" * 15)

termos = int(input("Quantos termos você quer ver?"))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2), end="")
cont = 3
while cont <= termos:
    t3 = t2 + t1
    print(" -> {}".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
print(" -> Fim!")

l = float(input("Digite a largura da parede em metros:"))
h = float(input("Digite a altura da parede em metros:"))
a = l * h
q = a / 2

print("Para pintar sua parede de {:.2f} metros quadrados, serão necessários {:.1f} litros de tinta." .format(a, q))

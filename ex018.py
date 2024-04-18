from math import radians, cos, tan, sin
ang = float(input("Digite o ângulo desejado:"))
seno = sin(radians(ang))
print("O SENO de {}º é {:.2f}.".format(ang, seno))
cosseno = cos(radians(ang))
print("O COSSENO de {}º é {:.2f}.".format(ang, cosseno))
tangente = tan(radians(ang))
print("A TANGENTE de {}º é {:.2f}.".format(ang, tangente))


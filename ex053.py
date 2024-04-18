"""str = input("Escreva uma frase:").strip().upper().replace(" ", "")
print("{} ao inverso fica {}.".format(str, "".join(reversed(str))))
if str == "".join(reversed(str)):
    print("{} É um palíndromo.".format(str))
else:
    print("{} NÃO é um palíndromo.".format(str))"""
frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("{} ao inverso fica {}.".format(junto, inverso))
if junto == inverso:
    print("{} É um palíndromo!".format(junto))
else:
    print("{} NÃO é um palíndromo!".format(junto))


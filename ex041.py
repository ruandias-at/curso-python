ano = int(input("Digite o seu ano de nascimento:"))
idade = 2024 - ano
if idade <= 9:
    print("Categoria Mirim.")
elif 14 >= idade > 9:
    print("Categoria Infantil.")
elif 19 >= idade > 14:
    print("Categoria Júnior.")
elif idade == 20:
    print("Categoria Sênior.")
else:
    print("Categoria Master.")

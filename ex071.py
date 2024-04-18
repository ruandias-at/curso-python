total50 = total20 = total10 = total1 = 0
print("=" * 30)
print("BANCO DO RUAS")
print("=" * 30)
saque = int(input("Quanto você quer sacar?"))
while True:
    if saque / 50 >= 1:
        total50 = saque // 50
        print(f"{total50} cédula(s) de R$50,00")
        saque = saque % 50
    if saque / 20 >= 1:
        total20 = saque // 20
        print(f"{total20} cédula(s) de R$20,00")
        saque = saque % 20
    if saque / 10 >= 1:
        total10 = saque // 10
        print(f"{total10} cédula(s) de R$10,00")
        saque = saque % 10
    if saque / 1 >= 1:
        total1 = saque
        print(f"{total1} cédula(s) de R$1,00")
        saque = saque % 1
    if saque == 0:
        break
print("Fim")

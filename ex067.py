while True:
    n = int(input(f"Quer ver a tabuada de que número?"))
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c} = {n * c}")
print("Programa encerrado.")

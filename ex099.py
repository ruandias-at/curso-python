from time import sleep
def lin():
    print("-=" * 25)

def maior(* num):
    cont = m = 0
    lin()
    print("Analisando os valores passados... ")
    lin()
    for valor in num:
        print(f"{valor}", end=' ', flush=True)
        sleep(0.4)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    print()
    lin()
    print(f"Foram informados {cont} valores ao todo.")
    lin()
    print(f"O maior valor informado foi {m}.")            
    lin()

# Programa Principal
maior(9, 2, 3, 4, 6)
maior(2, 5, 0, 8)
maior()
maior(2, 6, 1) 

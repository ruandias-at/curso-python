from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1    
    print("-=" * 25)
    print(f"Contagem de {inicio} até o {fim} de {passo} em {passo}.")
    if inicio < fim: 
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont += passo 
        print("FIM!")
        print("-=" * 25)
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM!")
        print("-=" * 25)


# Programa Principal    
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input("Digite o valor do ínicio da contagem personalizada: "))
f = int(input("Digite o valor do fim da contagem personalizada: "))
p = int(input("Digite o valor de intervalo entre os número: "))
contador(i, f, p)    
def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


# Programa principal
txt = str(input("Digite uma palavra para ser formatada: "))
escreva(txt)
escreva("Ruan Dias")
escreva("Botafogo")
escreva("Francisco Dias Teixeira")    
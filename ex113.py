def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print("\033[31mO usuário não informou um número inteiro.\033[m")
            return 0
        except (TypeError, ValueError):
            print("\033[31mERRO: Digite somente um número inteiro!\033[m")
        else:
            return n
            

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(",","."))
        except KeyboardInterrupt:
            print("\033[31mO usuário não informou um número real.\033[m")
            return 0
        except (TypeError, ValueError):
            print("\033[31mERRO: Digite somente um número real!\033[m")
        else:
            return n
            

n1 = leiaInt("Digite um inteiro: ")
n2 = leiaFloat("Digite um real: ")
print(f"Você digitou o inteiro {n1} e o real {n2}")

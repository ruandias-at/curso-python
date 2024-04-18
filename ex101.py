def voto(ano):
    """ A função voto pega o ano de seu nascimento, calcula a sua idade 
    e retorna sua situação com relação ao direito de voto."""
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        return f"Você tem {idade} anos e NÃO vota!"
    elif 16 <= idade < 18 or idade >= 65:
        return f"Você tem {idade} anos e seu voto é OPCIONAL!"
    else:
        return f"Você tem {idade} anos e seu voto é OBRIGATÓRIO!"


def lin():
    print("-=" * 25)

#Programa Principal
lin()        
nasc = int(input("Digite seu ano de nascimento: "))
lin()
print(voto(nasc))
lin()
 
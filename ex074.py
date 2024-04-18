from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
print(f"Foram sorteados os valores {n}")
print(f"O maior valor sorteado foi {max(n)}, e o menor foi {min(n)}")

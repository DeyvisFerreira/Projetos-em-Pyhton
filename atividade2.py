def eh_primo(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input("Digite um número inteiro positivo maior que 1: "))

if eh_primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
def calcular_fatorial(num):
    if num == 0:
        return 1
    else:
        return num * calcular_fatorial(num - 1)

numero = int(input("Digite um número inteiro para calcular o fatorial: "))

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    print("O fatorial de", numero, "é", calcular_fatorial(numero))
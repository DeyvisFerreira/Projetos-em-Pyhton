def soma_pares_intervalo(num1, num2):
    soma = 0
    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            soma += num
    return soma

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma_pares = soma_pares_intervalo(numero1, numero2)

print("A soma de todos os números pares no intervalo de", numero1, "a", numero2, "é:", soma_pares)
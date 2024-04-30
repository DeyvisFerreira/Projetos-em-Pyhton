def contar_digitos(numero):
    return len(str(numero))

numero = int(input("Digite um número: "))

quantidade_digitos = contar_digitos(numero)

print("O número", numero, "possui", quantidade_digitos, "dígito(s).")
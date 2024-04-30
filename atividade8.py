def decimal_para_binario(numero):
    return bin(numero)

def decimal_para_octal(numero):
    return oct(numero)

def decimal_para_hexadecimal(numero):
    return hex(numero)

numero_decimal = int(input("Digite um número decimal: "))
print("Selecione o tipo de conversão:")
print("1. Decimal para Binário")
print("2. Decimal para Octal")
print("3. Decimal para Hexadecimal")

opcao = input("Digite sua escolha (1/2/3): ")

if opcao == '1':
    print("O número", numero_decimal, "em binário é:", decimal_para_binario(numero_decimal))
elif opcao == '2':
    print("O número", numero_decimal, "em octal é:", decimal_para_octal(numero_decimal))
elif opcao == '3':
    print("O número", numero_decimal, "em hexadecimal é:", decimal_para_hexadecimal(numero_decimal))
else:
    print("Opção inválida.")
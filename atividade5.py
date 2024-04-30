def celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

def fahrenheit_para_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

print("Selecione a conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

escolha = input("Digite sua escolha (1/2): ")

if escolha == '1':
    temp_celsius = float(input("Digite a temperatura em Celsius: "))
    print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(temp_celsius))
elif escolha == '2':
    temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    print("Temperatura em Celsius:", fahrenheit_para_celsius(temp_fahrenheit))
else:
    print("Opção inválida.")
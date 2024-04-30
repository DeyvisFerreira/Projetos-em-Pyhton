def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

ano = int(input("Digite um ano para verificar se é bissexto: "))

if eh_bissexto(ano):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
# Um número primo circular é um número primo que 
# permanece primo mesmo após qualquer rotação de seus dígitos. 
# Por exemplo, o número 197 é um primo circular porque todas as 
# suas rotações (197, 971 e 719) também são primos.



def GeraRotacoes(numero):
    listaDePossibilidades = []
    numeroEmString = str(numero)
    tamanho = len(numeroEmString)
    flagPrimo = 0
    flagPrimoCircular = 0
    rotacoesInt = []

    for i in range(tamanho):
        rotacao = numeroEmString[i:] + numeroEmString[:i]
        listaDePossibilidades.append(rotacao)

    for val in listaDePossibilidades:
        rotacoesInt.append(int(val))
    return rotacoesInt

def VerificaPrimo(m):
    flagPrimo = 0
    for l in range(m):
        if l > 0 and m % l == 0:
            print(f"{m} e divisivel por {l}")
            flagPrimo += 1
    if flagPrimo == 2:
        print("primo")
    else:
        print("Nao primo")

def VerificaPrimoCircular(numero):
    rotacoes  = GeraRotacoes(numero)
    print(rotacoes)
    flagPrimo = 0 
    flagPrimoCircular = 0

    for numeros in rotacoes:
        for digito in range(numeros):
            if digito > 0 and numeros % digito == 0 :
                flagPrimo += 1
            if flagPrimo == 1:
                flagPrimoCircular += 1
            flagPrimo = 0
    if flagPrimoCircular == len(rotacoes):
        print(f"{rotacoes[0]} eh primo circular")
    else:
        print("nao eh primo circular")

VerificaPrimoCircular(119)
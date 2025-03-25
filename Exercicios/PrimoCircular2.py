def GeraRotacao(numero):
    rotacoes = []
    numeroEmString = str(numero)
    for i in range(len(numeroEmString)):
        rotacao = numeroEmString[i:]+numeroEmString[:i]
        rotacoes.append(int(rotacao))
    return rotacoes

def VerificaPrimo(numero):
    flagSouPrimo = 0

    for i in range(numero):
        if i>0 and numero % i == 0:
            flagSouPrimo+=1
    if flagSouPrimo == 1:
        return True
    else: 
        return False
    
def VerificaPrimoCircular(numeros):
    flagPrimoCircular = 0
    for i in numeros:
        if VerificaPrimo(i) == True:
            flagPrimoCircular+=1
    if flagPrimoCircular == len(numeros):
        return True
    else:
        return False
    
print(VerificaPrimoCircular([100,234,154]))
def PrimoCircular2(numero):
    primosCirculares = []
    for m in range(numero):
        rotacoes = GeraRotacao(m)
        if VerificaPrimoCircular(rotacoes) == True:
            primosCirculares.append(m)
        
    return primosCirculares

print(PrimoCircular2(1000))
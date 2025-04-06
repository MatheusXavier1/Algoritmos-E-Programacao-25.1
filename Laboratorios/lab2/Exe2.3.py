def ListaFibonacci(num):
    num1,num2 = 0,1
    listaSequencia = []
    
    while num1<=num:
        listaSequencia.append(num1)
        num1,num2 = num2,num1+num2

    return listaSequencia

def SomaListaFibonacci(lista):
    return sum(lista)

entrada = int(input())

print(ListaFibonacci(entrada))
print(SomaListaFibonacci(ListaFibonacci(entrada)))
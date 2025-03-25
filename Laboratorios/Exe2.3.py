def SequenciaDeFibonacci(num):
    num1,num2 = 0,1
    listaSequencia = []
    somaLista = 0
    listaSequencia.append(num1)
    listaSequencia.append(num2)

    for i in range(num):
        num3 = num1+num2
        
        listaSequencia.append(num3)

        num1 = num2
        num2 = num3

        if(num3>num):
            listaSequencia.pop()
            for i in listaSequencia:
                somaLista += i
            print(listaSequencia)
            print(somaLista)
            return 0 

SequenciaDeFibonacci(9)

def BubbleSort(minhaLista):
    tamanhoDaLista = len(minhaLista) - 1
    for x in range(tamanhoDaLista,0,-1):
        for j in range(x):
            if minhaLista[j] > minhaLista[j+1]:
                minhaLista[j],minhaLista[j+1] = minhaLista[j+1],minhaLista[j]

minhaLista = [4,1,2,98,34,12,0]
print(minhaLista)
BubbleSort(minhaLista)
print(minhaLista)
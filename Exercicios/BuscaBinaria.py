def BuscaBinaria(lista, item, inicio, fim):
    if inicio > fim:
        return print(f"{item} nao pertece a lista passada")
    
    meio = (inicio+fim)//2

    if lista[meio] == item:
        return meio
    
    elif lista[meio] < item:
        return BuscaBinaria(lista, item, meio+1, fim)
    
    elif lista[meio] > item:
        fim = meio -1
        return BuscaBinaria(lista,item,inicio,meio-1)

    
minhaLista = [1,2,3,4,5,6,10,12,14]
inicioDaLista = 0
fimDaLista = len(minhaLista)-1

print(BuscaBinaria(minhaLista,15,inicioDaLista,fimDaLista))
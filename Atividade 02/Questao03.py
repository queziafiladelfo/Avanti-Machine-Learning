#Função que retorna os elementos que estão presentes em apenas uma das listas
def elementos_unicos(lista1, lista2):
    return list(set(lista1).symmetric_difference(set(lista2)))


lista1 = [1, 2, 3, 4, 5, 10, 11, 15, 17, 29, 31]
lista2 = [1, 2, 3, 4, 5, 10, 11, 15, 17, 29, 30]
print(elementos_unicos(lista1, lista2)) 
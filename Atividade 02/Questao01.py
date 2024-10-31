
def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

lista = [1, 2, 3, 4, 5]
print(numeros_impares(lista))
def verifica_primo(n):
    if n <= 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

    
def numeros_primos(lista):
    return [n for n in lista if verifica_primo(n)]


numeros = [1, 2, 3, 4, 5, 10, 11, 15, 17, 29, 30]
primos = numeros_primos(numeros)
print(primos) 
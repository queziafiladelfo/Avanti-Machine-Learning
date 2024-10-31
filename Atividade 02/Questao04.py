def segundo_maior(lista):
    lista_unica = list(set(lista))

    if len(lista_unica) < 2:
        return None 

    lista_unica.remove(max(lista_unica))
    
    return max(lista_unica)


lista = [10, 20, 4, 45, 99]
resultado = segundo_maior(lista)
print(resultado)
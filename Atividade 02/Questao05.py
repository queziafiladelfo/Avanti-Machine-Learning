def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[0])

pessoas = [("Maria", 25), ("Ana", 30), ("João", 22)]
ordenadas = ordenar_por_nome(pessoas)
print(ordenadas)
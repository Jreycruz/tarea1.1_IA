def eliminarRepetidos(lista):
    
    conjunto = set(lista)
    ordenada = sorted(conjunto)
    return ordenada

entrada = [4, 2, 7, 4, 2, 1, 9, 7]
resultado = eliminarRepetidos(entrada)
print(resultado)


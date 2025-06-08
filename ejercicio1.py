def encontrar_mayor(lista):
    if not lista:
        return None

    mayor = lista[0] 
    for numero in lista[1:]:
        if numero > mayor:
            mayor = numero
    return mayor

numeros = [3, 9, 4, 1, 15]
resultado = encontrar_mayor(numeros)
print("El número mayor es:", resultado)

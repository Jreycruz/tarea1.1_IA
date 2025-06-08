def tabla_multiplicar():
    numero = int(input("Ingresa un número: "))
    i = 1
    while i <= 10:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        i += 1

tabla_multiplicar()

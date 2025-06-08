
ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

def sumarVentas(ventas):
    resultado = {}
    productos = ventas['Producto']
    cantidades = ventas['Cantidad']

    for i in range(len(productos)):
        producto = productos[i]
        cantidad = cantidades[i]
        if producto in resultado:
            resultado[producto] = resultado[producto] + cantidad 
        else:
            resultado[producto] = cantidad
    return resultado

ventaTotal = sumarVentas(ventas)
print(ventaTotal)

#Elaborar un programa en Python que permita gestionar el inventario de un supermercado el cual permite registrar compras (suman productos en el inventario), ventas (restan al inventario de productos), el programa debe tener 2 opciones una de compra y otra de ventas, el programa debe validar que no se vendan productos que no tengan existencias es decir si tengo un producto tv y tiene 5 elementos disponibles no permita vender ejemplo 10 porque no posee la cantidad disponible, por otra parte se deben registrar los datos del producto código, nombre, existencias, precio unitario.

inventario = {}

def agregar_o_actualizar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad de productos: "))
    precio = float(input("Ingrese el precio unitario del producto: "))
    
    if codigo in inventario:
        inventario[codigo]['existencias'] += cantidad
        inventario[codigo]['precio'] = precio
        print(f"Producto actualizado: {nombre}, existencias actuales: {inventario[codigo]['existencias']}.")
    else:
        inventario[codigo] = {'nombre': nombre, 'existencias': cantidad, 'precio': precio}
        print(f"Producto agregado: {nombre}, cantidad: {cantidad}.")

def vender_producto():
    codigo = input("Ingrese el código del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    
    if codigo not in inventario:
        print("Producto no encontrado en el inventario.")
        return
    
    if inventario[codigo]['existencias'] < cantidad:
        print(f"No hay suficientes existencias de {inventario[codigo]['nombre']} para vender. Disponibles: {inventario[codigo]['existencias']}.")
    else:
        inventario[codigo]['existencias'] -= cantidad
        print(f"Producto vendido: {inventario[codigo]['nombre']}, cantidad vendida: {cantidad}, existencias restantes: {inventario[codigo]['existencias']}.")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    for codigo, info in inventario.items():
        print(f"Código: {codigo}, Nombre: {info['nombre']}, Existencias: {info['existencias']}, Precio: {info['precio']}")

def main():
    while True:
        print("\nOpciones:")
        print("1. Registrar compra de producto")
        print("2. Registrar venta de producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_o_actualizar_producto()
        elif opcion == '2':
            vender_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()


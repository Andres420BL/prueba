'''
inventario de un supermercado 
registrar compras (suman productos en el inventario), 
ventas (restan al inventario de productos), 

2 opciones una de compra y otra de ventas, 

validar que no se vendan productos que no tengan existencias 

registrar los datos del producto código, nombre, existencias, precio unitario.
'''
import os

# Inicialización de productos?
codigoTV = '01'
nombreTV = 'Televisor'
existenciasTV = 0
precioTV = 500

codigoReloj = '02'
nombreReloj = 'Reloj'
existenciasReloj = 0
precioReloj = 50

control = True


while control:
    os.system('cls')
    # Menú
    print(f'\t.:Inventario actual:.\nProducto (existencias):.\n')
    # Mostrar todos los productos con sus existencias
    print(f'⮞ {nombreTV} #{codigoTV}: ({existenciasTV})')
    print(f'⮞ {nombreReloj} #{codigoReloj}: ({existenciasReloj})')
    print('..............................................................')

    
    opcion = int(input('\n[0]Salir\n[1]Registrar compras\n[2]Registrar ventas\n-->['))
    #Registrar compra de producto
    if opcion == 1:
        codigo= input('Código del producto --> ')
        cantidad = int(input('Cantidad de producto--> '))
        #Compra TV
        if codigo == codigoTV:
            existenciasTV += cantidad
            print(f'{nombreTV} ({cantidad}) ✔ Compra exitosa')
        #Compra Reloj
        elif codigo == codigoReloj:
            existenciasReloj += cantidad
            print(f'{nombreReloj} ({cantidad}) ✔ Compra exitosa')
        else:
            print('Producto no encontrado')
        input('Enter para continuar')
        
    elif opcion == 2:
        codigo= input('Código del producto --> ')
        cantidad = int(input('Cantidad de producto a vender --> '))
        #Venta TV
        if codigo == codigoTV:
            if existenciasTV >= cantidad:
                existenciasTV -= cantidad
                print(f'{nombreTV} ({cantidad}) ✔ Venta exitosa')
            else:
                print('ⓧ Error en la venta \nNo hay suficientes existencias ') 
                
        #Venta Reloj        
        elif codigo == codigoReloj:
            if existenciasReloj >= cantidad:
                existenciasReloj -= cantidad
                print(f'{nombreReloj} ({cantidad}) ✔ Venta exitosa')   
            else:
                print('ⓧ Error en la venta \nNo hay suficientes existencias ') 
        else:
            print('ⓧ Producto no encontrado')
            
        input('Enter para continuar')
            
            
            
            
        
        
   
        
        
    
        
            
    
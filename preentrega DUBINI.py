# Sistema de Gestión Básica De Productos
productos = []

while True:
    print("\nSistema de Gestión Básica De Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    # Opción 1: Agregar producto
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        while nombre.strip() == "":
            print("Error: El nombre no puede estar vacío")
            nombre = input("Nombre del producto: ")
        
        categoria = input("Categoría del producto: ")
        while categoria.strip() == "":
            print("Error: La categoría no puede estar vacía")
            categoria = input("Categoría del producto: ")
        
        precio = input("Precio del producto (sin centavos): ")
        while precio.strip() == "":
            print("Error: El precio no puede estar vacío")
            precio = input("Precio del producto (sin centavos): ")
        
        productos.append([nombre, categoria, int(precio)])
        print("Producto agregado correctamente")
    
    # Opción 2: Mostrar productos
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            print("\nLista de productos:")
            i = 1
            for producto in productos:
                print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")
                i += 1
    
    # Opción 3: Buscar productos
    elif opcion == "3":
        busqueda = input("Ingrese el nombre a buscar: ")
        encontrados = []
        for producto in productos:
            if busqueda in producto[0]:
                encontrados.append(producto)
        
        if len(encontrados) == 0:
            print("No se encontraron productos")
        else:
            print("\nProductos encontrados:")
            i = 1
            for producto in encontrados:
                print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")
                i += 1
    
    # Opción 4: Eliminar productos
    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos para eliminar")
        else:
            print("\nLista de productos:")
            i = 1
            for producto in productos:
                print(f"{i}. {producto[0]}")
                i += 1
            indice = int(input("Ingrese el número del producto a eliminar: ")) - 1
            producto_eliminado = productos[indice]  # Esto puede fallar si el índice no existe
            productos.pop(indice)
            print(f"Producto '{producto_eliminado[0]}' eliminado correctamente")
    
    # Opción 5: Salir
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Intente nuevamente")
# TRABAJO PRACTICO INTEGRADOR - PROGRAMACION 1
# Sistema de Control de Inventario
# En este trabajo se construye un programa con menú interactivo que controle el inventario de una ferretería, y se explica cómo se pensó en un informe y en un video.

def cargar_herramientas (inventario):
    print("\nCARGADO DE HERRAMIENTAS")
    
    while True:
        try:
            cantidad_herramientas = int(input("¿Cuántas herramientas desea cargar?: "))

            if cantidad_herramientas <= 0:
                raise ValueError("Debe ingresar un número mayor que cero.")

            break

        except ValueError as error:
            print("Error:", error)

    for i in range (cantidad_herramientas):
        while True:
            try:
                nombre = input ("Ingresa el nombre de la herramienta: ").strip()

                if nombre == "":
                    raise ValueError("El nombre no puede estar vacío.")

                for producto in inventario:
                    if producto["herramienta"].lower() == nombre.lower():
                        raise ValueError ("Esta herramienta ya existe.")

                break

            except ValueError as error:
                print("Error:", error)

        while True:
            try:
                cantidad = int(input("Ingresa la cantidad inicial: "))

                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")

                break

            except ValueError as error:
                print("Error:", error)

        inventario.append({"herramienta": nombre, "cantidad": cantidad})

        print("Herramienta/s cargada/s correctamente.")

def mostrar_inventario (inventario):
    print("\nINVENTARIO DE HERRAMIENTAS")

    if len (inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")

    else:
        for producto in inventario:
            print(f"Herramienta: {producto['herramienta']} - Cantidad: {producto['cantidad']}")

def consultar_stock (inventario):
    print("\nCONSULTA DE STOCK")

    if len (inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")

    else:
        nombre = input("Ingresa el nombre de la herramienta: ").strip()

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        encontrado = False

        for producto in inventario:
            if producto["herramienta"].lower() == nombre.lower():
                print(f"Stock disponible de {producto['herramienta']}: {producto['cantidad']}")
                encontrado = True

        if encontrado == False:
            print(f"La herramienta {nombre} no se encuentra en el inventario.")

def reporte_agotados (inventario):
    print("\nREPORTE DE HERRAMIENTAS AGOTADAS")

    if len (inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")

    else:
        agotados = 0

        for producto in inventario:
            if producto["cantidad"] == 0:
                print(f"Herramienta agotada: {producto['herramienta']}")
                agotados += 1

        if agotados == 0:
            print("No hay herramientas agotadas.")

def agregar_producto (inventario):
    print("\nAGREGAR NUEVO PRODUCTO")

    nombre = input("Ingresa el nombre de la herramienta: ").strip()

    if nombre == "":
        raise ValueError("El nombre no puede estar vacío.")

    for producto in inventario:
        if producto["herramienta"].lower() == nombre.lower():
            raise ValueError("Esta herramienta ya existe.")

    cantidad = int(input("Ingresa la cantidad inicial: "))

    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    inventario.append({"herramienta": nombre, "cantidad": cantidad})

    print(f"Herramienta {nombre} agregada correctamente con {cantidad} unidades.")

def actualizar_stock (inventario):
    print("\nACTUALIZAR STOCK")

    if len (inventario) == 0:
        print("No hay herramientas cargadas en el inventario.")

    else:
        nombre = input("Ingresa el nombre de la herramienta: ").strip()

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        encontrado = False

        for producto in inventario:
            if producto["herramienta"].lower() == nombre.lower():
                encontrado = True
                herramienta = producto

        if encontrado == False:
            print(f"La herramienta {nombre} no se encuentra en el inventario.")

        else:
            movimiento = input("Ingresa el tipo de movimiento (venta/ingreso): ").strip().lower()

            if movimiento == "venta" or movimiento == "ingreso":
                cantidad = int(input("Ingresa la cantidad de unidades: "))

                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor que cero.")

                if movimiento == "venta":
                    if cantidad > herramienta["cantidad"]:
                        raise ValueError("No hay stock suficiente para realizar la venta.")

                    herramienta["cantidad"] -= cantidad

                else:
                    herramienta["cantidad"] += cantidad

                print(f"Stock actualizado correctamente. Nuevo stock: {herramienta['cantidad']}")

            else:
                print("Tipo de movimiento inválido. Debe ingresar venta o ingreso.")


def main():
    inventario = []
    opcion = 0

    while opcion != 7:
        print ("\n===== SISTEMA DE CONTROL DE INVENTARIO =====")
        print ("1. Cargar herramientas con existencias iniciales")
        print ("2. Visualizar inventario")
        print ("3. Consultar stock")
        print ("4. Reporte de herramientas agotadas")
        print ("5. Agregar un nuevo producto")
        print ("6. Actualizar stock (venta/ingreso)")
        print ("7. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))

            if opcion == 7:
                print ("Saliendo del sistema...")

            elif opcion < 1 or opcion > 7:
                raise ValueError ("Debe ingresar una opción del 1 al 7.")

            elif opcion == 1:
                cargar_herramientas(inventario)

            elif opcion == 2:
                mostrar_inventario(inventario)

            elif opcion == 3:
                consultar_stock(inventario)

            elif opcion == 4:
                reporte_agotados(inventario)

            elif opcion == 5:
                agregar_producto(inventario)

            elif opcion == 6:
                actualizar_stock(inventario)

        except ValueError as error:
            print("Error:", error)


main()

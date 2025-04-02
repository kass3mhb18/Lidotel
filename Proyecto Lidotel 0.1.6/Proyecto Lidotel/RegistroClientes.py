import os
from VerRegistrosClientes import menu_ver_modificar_registros

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def verificar_o_crear_archivo_individual(nombre_archivo_individual):
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo_individual):
        # Si no existe, crear el archivo
        with open(nombre_archivo_individual, "w") as archivo:         
            pass  
    else:
        pass  

# Nombre del archivo a verificar
nombre_del_archivo_individual = "clientes_individuales.txt"


def verificar_o_crear_archivo_acompanados(nombre_archivo_acompanados):
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo_acompanados):
        # Si no existe, crear el archivo
        with open(nombre_archivo_acompanados, "w") as archivo:
            pass  # Crear el archivo vacío

# Nombre del archivo a verificar
nombre_del_archivo_acompanados = "clientes_acompanados.txt"


def verificar_o_crear_archivo_grupo_familia(nombre_archivo_grupo_familia):
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo_grupo_familia):
        # Si no existe, crear el archivo
        with open(nombre_archivo_grupo_familia, "w") as archivo:         
            pass  
    else:
        pass  

# Nombre del archivo a verificar
nombre_del_archivo_grupo_familia = "clientes_grupo_familia.txt"

# Función para validar si el campo contiene solo letras
def validar_entrada_alfabetica(entrada):
    return entrada.isalpha()


# Función para validar si el campo contiene solo números
def validar_entrada_numerica(entrada):
    return entrada.isdigit()


def registrar_cliente_individual():
    nombre_del_archivo_individual = "clientes_individuales.txt"
    nombre_del_archivo_acompanados = "clientes_acompanados.txt"
    nombre_del_archivo_grupo_familia = "clientes_grupo_familia.txt"

    # Verificar si el archivo de clientes existe antes de iniciar
    verificar_o_crear_archivo_individual(nombre_del_archivo_individual)

    # Pedir datos del cliente
    while True:
        nombre = input("|Nombre: ")
        if not validar_entrada_alfabetica(nombre):
            print("|El nombre solo puede contener letras. Intente de nuevo.")
            continue
        break

    while True:
        apellido = input("|Apellido: ")
        if not validar_entrada_alfabetica(apellido):
            print("|El apellido solo puede contener letras. Intente de nuevo.")
            continue
        break

    while True:
        cedula = input("|Cédula: ")

        # Validar que la cédula solo contenga números
        if not validar_entrada_numerica(cedula):
            print("|Cédula inválida. Debe contener solo números. Intente de nuevo.")
            continue

        # Verificar si la cédula ya está registrada en algún archivo
        archivos_a_verificar = [
            nombre_del_archivo_individual,
            nombre_del_archivo_acompanados,
            nombre_del_archivo_grupo_familia
        ]

        cedula_existente = False
        for archivo in archivos_a_verificar:
            try:
                with open(archivo, "r") as file:
                    registros = file.readlines()
                    for registro in registros:
                        datos = registro.strip().split(",")
                        if len(datos) > 2 and datos[2] == cedula:
                            print(f"|Error: Ya existe un registro con esta cédula en {archivo}.")
                            cedula_existente = True
                            break
                    if cedula_existente:
                        break
            except FileNotFoundError:
                continue  # Si el archivo no existe, continuar con la validación

        if cedula_existente:
            continue  # Volver a pedir la cédula si ya está registrada

        # Si la cédula no está registrada, continuar con el registro
        break


    while True:
        email = input("|Email: ")
        if '@' not in email or '.' not in email:
            print("|Email no válido. Intente de nuevo.")
            continue
        break

    while True:
        telefono = input("|Teléfono: ")
        if not validar_entrada_numerica(telefono) or len(telefono) < 10:
            print("|Teléfono no válido. Intente de nuevo.")
            continue
        break

    while True:
        dias_estadia = input("|Cantidad de días de estadía: ")
        if not dias_estadia.isdigit() or int(dias_estadia) <= 0:
            print("|Días de estadía no válidos. Intente de nuevo.")
            continue
        dias_estadia = int(dias_estadia)
        break

    limpiar_consola()
    # Mostrar habitaciones disponibles
    print(f"Cliente {nombre} {apellido} C.I {cedula}")
    print(" ______________________________________ ")
    print("|       Selección de habitaciones      |")
    print("|______________________________________|")
    print("| (1). SENCILLA - 60$ por noche        |")
    print("| (2). DOBLE - 120$ por noche          |")
    print("| (3). FAMILY ROOM - 200$ por noche    |")
    print("| (4). SUITE - 300$ por noche          |")
    print("|______________________________________|")

    # Ingresar la selección con validación
    while True:
        try:
            seleccion = int(input("|Ingrese el número de la habitación seleccionada: "))
            
            if seleccion == 1:
                habitacion_seleccionada = "SENCILLA"    

                descripcion_habitacion = """|Amplia y confortable habitación decorada con un estilo vanguardista, cama Lidotel 
|Royal King con sábanas de algodón egipcio, soporte para iPod con reloj despertador, 
|TV 32” HD Plasma con cable, baño con ducha, cafetera eléctrica, nevera ejecutiva, caja 
|electrónica de seguridad y secador de cabello."""

                incluidos_habitacion = """|Desayuno Buffet en Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|acceso a las instalaciones del Business Center, uso de nuestra exclusiva piscina, 
|acceso a nuestro moderno gimnasio y Kit de vanidades. Niños de 0 a 2 años sin recargos."""
                precio_noche = 60
                break
            elif seleccion == 2:
                habitacion_seleccionada = "DOBLE"

                descripcion_habitacion = """|Amplia y confortable habitación decorada con un estilo vanguardista, Dos Camas 
|Lidotel Full con sábanas de algodón egipcio, soporte para iPod con reloj despertador, 
|TV 32” HD Plasma con cable, baño con ducha, cafetera eléctrica, nevera ejecutiva, caja 
|electrónica de seguridad y secador de cabello."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|acceso a las instalaciones del Business Center, uso de nuestra exclusiva piscina, 
|acceso a nuestro moderno gimnasio y Kit de vanidades. Niños de 0 a 2 años sin recargos."""
                precio_noche = 120
                break
            elif seleccion == 3:
                habitacion_seleccionada = "FAMILY ROOM"

                descripcion_habitacion = """|Cálida y confortable habitación decorada con un estilo vanguardista, 100 porciento libre de 
|humo, cama Lidotel Royal King, con reloj despertador, TV 32” HD Plasma con cable, 
|baño con ducha, cafetera eléctrica, nevera ejecutiva, caja electrónica de seguridad y 
|secador de cabello, armario adicional amplio, una habitación separada con 2 camas full, baño con ducha."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|Business Center, uso de nuestra exclusiva piscina, acceso a nuestro gimnasio, sillas y 
|toldos en la playa, kit de vanidades y niños de 0 a 2 años sin recargos."""
                precio_noche = 200
                break
            elif seleccion == 4:
                habitacion_seleccionada = "SUITE"

                descripcion_habitacion = """|Cálida y confortable habitación decorada con un estilo vanguardista, 100 porciento libre de 
|humo, Cama Lidotel Royal King, con reloj despertador, TV 32” HD Plasma con cable, 2 
|baños con ducha, cafetera eléctrica, nevera ejecutiva, caja electrónica de seguridad y 
|secador de cabello, armario adicional amplio y área separada con 2 sofá-cama individuales."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|Business Center, uso de nuestra exclusiva piscina, acceso a nuestro gimnasio, sillas y 
|toldos en la playa, kit de vanidades y niños de 0 a 2 años sin recargos."""
                precio_noche = 300
                break
            else:
                print("|Selección inválida. Por favor, seleccione un número entre 1 y 4.")
        except ValueError:
            print("|Por favor, ingrese solo números válidos.")

    # Si la selección es válida, calcular el total de la estadía
    if habitacion_seleccionada:
        limpiar_consola()
        print(f"|---                Has seleccionado la habitacion {habitacion_seleccionada}       ---|\n")
        print("|---                                DESCRIPCION                               ---|\n")
        print(f"{descripcion_habitacion}\n")
        print("|---                                  INCLUYE                                 ---|\n")
        print(f"{incluidos_habitacion}\n")
        input("Presione Enter para continuar...")
        total_estadia = precio_noche * dias_estadia
        limpiar_consola()
        print(f"|Factura Lidotel:\n|Nombre: {nombre} {apellido}\n|Cédula: {cedula}\n|Email: {email}\n|Teléfono: {telefono}")
        print(f"|Estadía: {dias_estadia} días\n|Precio por noche: {precio_noche}$\n|Habitación: {habitacion_seleccionada}\n|Total: {total_estadia}$")
        
        # Realizar el pago
        while True:
            try:
                pago = float(input(f"\n|Ingrese el monto a pagar: "))
                
                if pago < total_estadia:
                    print(f"|El pago es insuficiente de {total_estadia}$ faltan ({total_estadia - pago}$) Intente de nuevo.")
                elif pago > total_estadia:
                    vuelto = pago - total_estadia
                    print(f"|Pago realizado correctamente. Su vuelto es: {vuelto}$")
                    break
                else:
                    print("|Pago realizado correctamente. Total exacto.")
                    break
            except ValueError:
                print("|Por favor, ingrese un monto válido.")

        # Guardar la información en el archivo de clientes
        with open(nombre_del_archivo_individual, "a") as file:
            file.write(f"{nombre},{apellido},{cedula},{email},{telefono},{dias_estadia},{habitacion_seleccionada},{total_estadia}\n")
    else:
        print("Opción de habitación no válida.")




def registrar_cliente_acompanado():
    nombre_del_archivo_acompanados = "clientes_acompanados.txt"
    nombre_del_archivo_individual = "clientes_individuales.txt"
    nombre_del_archivo_grupo_familia = "clientes_grupo_familia.txt"

    clientes = []
    cedulas_registradas = []  # Lista para almacenar las cédulas registradas

    for i in range(2):
        print(f"\n|Registro de Cliente {i+1}|")

        # Validación para el nombre
        while True:
            nombre = input("|Nombre: ")
            if not validar_entrada_alfabetica(nombre):
                print("|El nombre solo puede contener letras. Intente de nuevo.")
                continue
            break

        # Validación para el apellido
        while True:
            apellido = input("|Apellido: ")
            if not validar_entrada_alfabetica(apellido):
                print("|El apellido solo puede contener letras. Intente de nuevo.")
                continue
            break

        # Validación para la cédula
        while True:
            cedula = input("|Cédula: ")

            # Validar que la cédula solo contenga dígitos
            if not validar_entrada_numerica(cedula):
                print("|Error: La cédula solo puede contener números.")
                continue

            # Verificar si la cédula ya está registrada en la sesión actual
            if cedula in cedulas_registradas:
                print("|Error: La cédula ya fue registrada para otro cliente.")
                continue

            # Verificar en archivos existentes
            archivos_a_verificar = [
                nombre_del_archivo_individual, 
                nombre_del_archivo_acompanados, 
                nombre_del_archivo_grupo_familia
            ]

            cedula_existente = False
            for archivo in archivos_a_verificar:
                try:
                    with open(archivo, "r") as file:
                        registros = file.readlines()
                        for registro in registros:
                            datos = registro.strip().split(",")
                            if len(datos) > 2 and datos[2] == cedula:
                                print(f"|Error: Ya existe un registro con esta cédula en {archivo}.")
                                cedula_existente = True
                                break
                        if cedula_existente:
                            break
                except FileNotFoundError:
                    continue  # Si el archivo no existe, seguir con la validación

            if cedula_existente:
                continue

            # Si la cédula no existe, agregarla a la lista de registradas y continuar
            cedulas_registradas.append(cedula)
            break


        # Validación para el email
        while True:
            email = input("|Email: ")
            if '@' not in email or '.' not in email:
                print("|Email no válido. Intente de nuevo.")
                continue
            break

        # Validación para el teléfono
        while True:
            telefono = input("|Teléfono: ")
            if not validar_entrada_numerica(telefono) or len(telefono) < 10:
                print("|Teléfono no válido. Intente de nuevo.")
                continue
            break

        # Agregar los datos del cliente a la lista
        clientes.append(f"{nombre},{apellido},{cedula},{email},{telefono}")

    # Al final, pedimos los días de estadía para ambos clientes
    while True:
        dias_estadia = input("|Cantidad de días de estadía: ")
        if not dias_estadia.isdigit() or int(dias_estadia) <= 0:
            print("|Días de estadía no válidos. Intente de nuevo.")
            continue
        dias_estadia = int(dias_estadia)
        break

    # Selección de habitación
    limpiar_consola()
    for cliente in clientes:
        # Separamos los datos del cliente (nombre, apellido, cédula, email, teléfono)
        datos_cliente = cliente.split(",")
        nombre = datos_cliente[0]
        apellido = datos_cliente[1]
        cedula = datos_cliente[2]    
        # Mostrar los datos del cliente dentro del bucle
        print(f"Cliente {nombre} {apellido} C.I {cedula}")

    
    print(" ______________________________________ ")
    print("|       Selección de habitaciones      |")
    print("|______________________________________|")
    print("| (1). DOBLE - 120$ por noche          |")
    print("| (2). FAMILY ROOM - 200$ por noche    |")
    print("| (3). SUITE - 300$ por noche          |")
    print("|______________________________________|")

    while True:
        try:
            seleccion = int(input("|Ingrese el número de la habitación seleccionada: "))

            if seleccion == 1:
                habitacion_seleccionada = "DOBLE"

                descripcion_habitacion = """|Amplia y confortable habitación decorada con un estilo vanguardista, Dos Camas 
|Lidotel Full con sábanas de algodón egipcio, soporte para iPod con reloj despertador, 
|TV 32” HD Plasma con cable, baño con ducha, cafetera eléctrica, nevera ejecutiva, caja 
|electrónica de seguridad y secador de cabello."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|acceso a las instalaciones del Business Center, uso de nuestra exclusiva piscina, 
|acceso a nuestro moderno gimnasio y Kit de vanidades. Niños de 0 a 2 años sin recargos."""
                precio_noche = 120
                break

            elif seleccion == 2:
                habitacion_seleccionada = "FAMILY ROOM"

                descripcion_habitacion = """|Cálida y confortable habitación decorada con un estilo vanguardista, 100 porciento libre de 
|humo, cama Lidotel Royal King, con reloj despertador, TV 32” HD Plasma con cable, 
|baño con ducha, cafetera eléctrica, nevera ejecutiva, caja electrónica de seguridad y 
|secador de cabello, armario adicional amplio, una habitación separada con 2 camas full, baño con ducha."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|Business Center, uso de nuestra exclusiva piscina, acceso a nuestro gimnasio, sillas y 
|toldos en la playa, kit de vanidades y niños de 0 a 2 años sin recargos."""
                precio_noche = 200
                break

            elif seleccion == 3:
                habitacion_seleccionada = "SUITE"

                descripcion_habitacion = """|Cálida y confortable habitación decorada con un estilo vanguardista, 100 porciento libre de 
|humo, Cama Lidotel Royal King, con reloj despertador, TV 32” HD Plasma con cable, 2 
|baños con ducha, cafetera eléctrica, nevera ejecutiva, caja electrónica de seguridad y 
|secador de cabello, armario adicional amplio y área separada con 2 sofá-cama individuales."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|Business Center, uso de nuestra exclusiva piscina, acceso a nuestro gimnasio, sillas y 
|toldos en la playa, kit de vanidades y niños de 0 a 2 años sin recargos."""
                precio_noche = 300
                break
            else:
                print("|Selección inválida. Por favor, seleccione un número entre 1 y 3.")
        except ValueError:
            print("|Por favor, ingrese solo números válidos.")


    if habitacion_seleccionada:
        limpiar_consola()
    print(f"|---                Has seleccionado la habitación {habitacion_seleccionada}       ---|\n")
    print("|---                                DESCRIPCIÓN                               ---|\n")
    print(f"{descripcion_habitacion}\n")
    print("|---                                  INCLUYE                                 ---|\n")
    print(f"{incluidos_habitacion}\n")
    input("Presione Enter para continuar...")

    total_estadia = precio_noche * dias_estadia

    # Limpiar la consola y mostrar la factura
    limpiar_consola()
    print("|Factura Lidotel:")

    # Imprimir la información de ambos clientes en la factura
    factura = ""
    for cliente in clientes:
        # Separar los datos de cada cliente
        datos_cliente = cliente.split(",")
        nombre = datos_cliente[0]
        apellido = datos_cliente[1]
        cedula = datos_cliente[2]
        email = datos_cliente[3]
        telefono = datos_cliente[4]

        # Concatenar la información de los clientes en la factura
        factura += f"\n|{nombre} {apellido} - C.I {cedula} | {email} | {telefono} "

    # Imprimir la factura con ambos clientes
    print(factura)

    # Información de la estadía
    print(f"|Estadía: {dias_estadia} días\n|Precio por noche: {precio_noche}$\n|Habitación: {habitacion_seleccionada}\n|Total: {total_estadia}$")
        # Realizar el pago

    while True:
            try:
                pago = float(input(f"\n|Ingrese el monto a pagar: "))
                
                if pago < total_estadia:
                    print(f"|El pago es insuficiente de {total_estadia}$ faltan ({total_estadia - pago}$) Intente de nuevo.")
                elif pago > total_estadia:
                    vuelto = pago - total_estadia
                    print(f"|Pago realizado correctamente. Su vuelto es: {vuelto}$")
                    break
                else:
                    print("|Pago realizado correctamente. Total exacto.")
                    break
            except ValueError:
                print("|Por favor, ingrese un monto válido.")   

    # Agregar los días de estadía y la habitación a los clientes
    for i in range(len(clientes)):
        clientes[i] = f"{clientes[i]},{dias_estadia},{habitacion_seleccionada}"

    # Guardar los datos en el archivo en líneas separadas
    with open(nombre_del_archivo_acompanados, "a") as file:
        for cliente in clientes:
            file.write(f"{cliente},{total_estadia}\n")

    print("|Registro completado exitosamente.")



def registrar_cliente_grupo_familiar():
    nombre_del_archivo_acompanados = "clientes_acompanados.txt"
    nombre_del_archivo_individual = "clientes_individuales.txt"
    nombre_del_archivo_grupo_familia = "clientes_grupo_familia.txt"

    clientes = []
    cedulas_registradas = []  # Lista para almacenar las cédulas registradas

    while True:
        try:
            cantidad_adultos = int(input("|Ingrese la cantidad de personas adultas en el grupo: "))
            if cantidad_adultos <= 0:
                print("|Error: Debe ingresar al menos un adulto.")
                continue
            break
        except ValueError:
            print("|Error: Ingrese un número válido.")

    for i in range(cantidad_adultos):
        print(f"\n|Registro de Adulto {i+1}|")

        while True:
            nombre = input("|Nombre: ")
            if not validar_entrada_alfabetica(nombre):
                print("|El nombre solo puede contener letras. Intente de nuevo.")
                continue
            break

        while True:
            apellido = input("|Apellido: ")
            if not validar_entrada_alfabetica(apellido):
                print("|El apellido solo puede contener letras. Intente de nuevo.")
                continue
            break

        while True:
            cedula = input("|Cédula: ")

            # Validar que la cédula solo contenga dígitos
            if not validar_entrada_numerica(cedula):
                print("|Error: La cédula solo puede contener números.")
                continue

            # Verificar si la cédula ya está registrada en la sesión actual
            if cedula in cedulas_registradas:
                print("|Error: La cédula ya fue registrada para otro cliente.")
                continue

            # Verificar si la cédula ya está registrada en algún archivo
            archivos_a_verificar = [
                nombre_del_archivo_individual,
                nombre_del_archivo_acompanados,
                nombre_del_archivo_grupo_familia
            ]

            cedula_existente = False
            for archivo in archivos_a_verificar:
                try:
                    with open(archivo, "r") as file:
                        registros = file.readlines()
                        for registro in registros:
                            datos = registro.strip().split(",")
                            if len(datos) > 2 and datos[2] == cedula:
                                print(f"|Error: Ya existe un registro con esta cédula en {archivo}.")
                                cedula_existente = True
                                break
                        if cedula_existente:
                            break
                except FileNotFoundError:
                    continue  # Si el archivo no existe, continuar con la validación

            if cedula_existente:
                continue  # Volver a pedir la cédula si ya está registrada

            # Si la cédula no está registrada, agregarla a la lista
            cedulas_registradas.append(cedula)
            break

        while True:
            email = input("|Email: ")
            if '@' not in email or '.' not in email:
                print("|Email no válido. Intente de nuevo.")
                continue
            break

        while True:
            telefono = input("|Teléfono: ")
            if not validar_entrada_numerica(telefono) or len(telefono) < 10:
                print("|Teléfono no válido. Intente de nuevo.")
                continue
            break

        clientes.append(f"{nombre},{apellido},{cedula},{email},{telefono}")

    while True:
        respuesta = input("|¿Posee hijos? (si/no): ").strip().lower()
        if respuesta in ["si", "no"]:
            tiene_hijos = respuesta == "si"
            break
        print("|Por favor, responda con 'si' o 'no'.")

    if tiene_hijos:
        while True:
            try:
                cantidad_hijos = int(input("|Ingrese la cantidad de hijos: "))
                if cantidad_hijos < 0:
                    print("|Error: La cantidad no puede ser negativa.")
                    continue
                break
            except ValueError:
                print("|Error: Ingrese un número válido.")

        for i in range(cantidad_hijos):
            print(f"\n|Registro de Hijo {i+1}|")
            while True:
                nombre_hijo = input("|Nombre: ")
                if not validar_entrada_alfabetica(nombre_hijo):
                    print("|El nombre solo puede contener letras. Intente de nuevo.")
                    continue
                break

            while True:
                apellido_hijo = input("|Apellido: ")
                if not validar_entrada_alfabetica(apellido_hijo):
                    print("|El apellido solo puede contener letras. Intente de nuevo.")
                    continue
                break

            while True:
                try:
                    edad_hijo = int(input("|Edad: "))
                    if edad_hijo <= 0:
                        print("|Error: La edad debe ser mayor a 0.")
                        continue
                    break
                except ValueError:
                    print("|Error: Ingrese una edad válida.")

            clientes.append(f"{nombre_hijo},{apellido_hijo},N/A,N/A,N/A,Edad:{edad_hijo}")

    while True:
        try:
            dias_estadia = int(input("|Cantidad de días de estadía: "))
            if dias_estadia <= 0:
                print("|Días de estadía no válidos. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("|Ingrese un número válido.")

    limpiar_consola()
    if clientes:
        print(f"\nCliente: {clientes[0]}")
    print(" ______________________________________ ")
    print("|       Selección de habitaciones      |")
    print("|______________________________________|")
    print("| (1). DOBLE - 120$ por noche          |")
    print("| (2). FAMILY ROOM - 200$ por noche    |")
    print("| (3). SUITE - 300$ por noche          |")
    print("|______________________________________|")

    while True:
        try:
            seleccion = int(input("|Ingrese el número de la habitación seleccionada: "))
            if seleccion == 1:
                habitacion_seleccionada = "DOBLE"

                descripcion_habitacion = """|Amplia y confortable habitación decorada con un estilo vanguardista, Dos Camas 
|Lidotel Full con sábanas de algodón egipcio, soporte para iPod con reloj despertador, 
|TV 32” HD Plasma con cable, baño con ducha, cafetera eléctrica, nevera ejecutiva, caja 
|electrónica de seguridad y secador de cabello."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|acceso a las instalaciones del Business Center, uso de nuestra exclusiva piscina, 
|acceso a nuestro moderno gimnasio y Kit de vanidades. Niños de 0 a 2 años sin recargos."""

                precio_noche = 120
                break
            elif seleccion == 2:
                habitacion_seleccionada = "FAMILY ROOM"

                descripcion_habitacion = """|Cálida y confortable habitación decorada con un estilo vanguardista, 100 porciento libre de 
|humo, cama Lidotel Royal King, con reloj despertador, TV 32” HD Plasma con cable, 
|baño con ducha, cafetera eléctrica, nevera ejecutiva, caja electrónica de seguridad y 
|secador de cabello, armario adicional amplio, una habitación separada con 2 camas full, baño con ducha."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|Business Center, uso de nuestra exclusiva piscina, acceso a nuestro gimnasio, sillas y 
|toldos en la playa, kit de vanidades y niños de 0 a 2 años sin recargos."""

                precio_noche = 200
                break
            elif seleccion == 3:
                habitacion_seleccionada = "SUITE"

                descripcion_habitacion = """|Cálida y confortable habitación decorada con un estilo vanguardista, 100 porciento libre de 
|humo, Cama Lidotel Royal King, con reloj despertador, TV 32” HD Plasma con cable, 2 
|baños con ducha, cafetera eléctrica, nevera ejecutiva, caja electrónica de seguridad y 
|secador de cabello, armario adicional amplio y área separada con 2 sofá-cama individuales."""

                incluidos_habitacion = """|Desayuno Buffet en el Restaurant Le Nouveau, acceso inalámbrico a Internet (WIFI), 
|Business Center, uso de nuestra exclusiva piscina, acceso a nuestro gimnasio, sillas y 
|toldos en la playa, kit de vanidades y niños de 0 a 2 años sin recargos."""

                precio_noche = 300
                break
            else:
                print("|Selección inválida. Por favor, seleccione un número entre 1 y 3.")
        except ValueError:
            print("|Por favor, ingrese solo números válidos.")
            
    if habitacion_seleccionada:
        limpiar_consola()
    print(f"|---                Has seleccionado la habitación {habitacion_seleccionada}       ---|\n")
    print("|---                                DESCRIPCIÓN                               ---|\n")
    print(f"{descripcion_habitacion}\n")
    print("|---                                  INCLUYE                                 ---|\n")
    print(f"{incluidos_habitacion}\n")
    input("Presione Enter para continuar...")


    total_estadia = precio_noche * dias_estadia

    limpiar_consola()
    print("|Factura Lidotel:")

    # Imprimir la información de ambos clientes en la factura
    factura = ""
    for cliente in clientes:
        # Separar los datos de cada cliente
        datos_cliente = cliente.split(",")
        nombre = datos_cliente[0]
        apellido = datos_cliente[1]
        cedula = datos_cliente[2]
        email = datos_cliente[3]
        telefono = datos_cliente[4]

        # Concatenar la información de los clientes en la factura
        factura += f"\n|{nombre} {apellido} - C.I {cedula} | {email} | {telefono} "

    # Imprimir la factura con ambos clientes
    print(factura)

    # Información de la estadía
    print(f"|Estadía: {dias_estadia} días\n|Precio por noche: {precio_noche}$\n|Habitación: {habitacion_seleccionada}\n|Total: {total_estadia}$")
    
    # Realizar el pago
    while True:
        try:
            pago = float(input(f"\n|Ingrese el monto a pagar: "))
            
            if pago < total_estadia:
                print(f"|El pago es insuficiente de {total_estadia}$ faltan ({total_estadia - pago}$). Intente de nuevo.")
            elif pago > total_estadia:
                vuelto = pago - total_estadia
                print(f"|Pago realizado correctamente. Su vuelto es: {vuelto}$")
                break
            else:
                print("|Pago realizado correctamente. Total exacto.")
                break
        except ValueError:
            print("|Por favor, ingrese un monto válido.")

    with open(nombre_del_archivo_grupo_familia, "a") as file:
        for cliente in clientes:
            file.write(f"{cliente},{dias_estadia},{habitacion_seleccionada},{total_estadia}\n")

    print("|Registro completado exitosamente.")




            
# Menú principal de registro
def menu_registro_clientes():
    # Verificar si el archivo de clientes existe antes de mostrar el menú
    
    # Llamar a la función
    verificar_o_crear_archivo_individual(nombre_del_archivo_individual)
    verificar_o_crear_archivo_acompanados(nombre_del_archivo_acompanados)
    verificar_o_crear_archivo_grupo_familia(nombre_del_archivo_grupo_familia)

    while True:
        limpiar_consola()
        print(" ______________________________________ ")
        print("| --- Menú de Registro de Clientes --- |")
        print("|______________________________________|")
        print("| (1). Registrar Individual            |")
        print("| (2). Registrar Acompañado            |")
        print("| (3). Registrar Grupo/Familia         |")
        print("| (4). Ver/Modificar Registros         |")
        print("| (5). Volver al menú principal        |")
        print("|______________________________________|")
        opcion = input("|Seleccione una opción: ")

        if opcion.isdigit():
            if opcion == "1":
                limpiar_consola()
                registrar_cliente_individual()
            elif opcion == "2":
                limpiar_consola()
                registrar_cliente_acompanado()
            elif opcion == "3":
                limpiar_consola()
                registrar_cliente_grupo_familiar()
                break
            elif opcion == "4":
                menu_ver_modificar_registros()
                break
            elif opcion == "5":
                print("\nRegresando al menú principal...")
                break
            else:
                print("\nOpción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")
        else:
            print("\nPor favor, ingrese un número válido.")
            input("\nPresione Enter para continuar...")




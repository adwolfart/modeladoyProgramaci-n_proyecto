import pymysql
import time

"""
funcion para conectarnos a la bd
"""
def conectarBD():
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="Coco27+1", db="Proyecto_A")
        return conn
    except:
        print("Error en la conexion de la BD")
        exit(0)

"""
funcion para desconectarnos de la bd
"""
def desConectarBD(conn):
    conn.commit()
    conn.close()

"""
verifica que no exista otro nombre igual en la bd
"""
def verificar_nombre_usuarios(nombreDado):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre_usuario, fk_id_perfil, pk_id_usuario FROM Usuarios")

        #fetchone()
        for nombre in cursor.fetchall():
            if nombreDado == nombre[0]:
                return True, nombre[1], nombre[2]
    except:
        print("Saliendo error en la base")
        exit(0)
    finally:
        desConectarBD(conn)
    return False, False, False

"""
inserta en la bd un nuevo usuario
"""
def registar_usuario_BD(nombre_usuario, id_perfil):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuarios (nombre_usuario, fk_id_perfil) VALUES (%s, %s)", (nombre_usuario, id_perfil))
    except:
        print("Saliendo error en la base")
        exit(0)
    finally:
        desConectarBD(conn)

"""
verifica en la bd que no exista un nombre de terminal igual
"""
def verificar_nombre_terminal(nombre_terminal):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_terminal, nombre_terminal FROM Terminal")

        #fetchone()
        for nombre in cursor.fetchall():
            if nombre_terminal == nombre[1]:
                return True
    except:
        print("Saliendo error en la base verificar_nombre_terminal")
        exit(0)
    finally:
        desConectarBD(conn)
    return False

"""
registra una terminal en la bd
"""
def registrar_terminal_BD(nombre_terminal, id_usuario):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Terminal (nombre_terminal, fk_id_usuario) VALUES (%s, %s)", (nombre_terminal, id_usuario))
    except:
        print("Saliendo error en la base")
        exit(0)
    finally:
        desConectarBD(conn)

"""
muestra todas las terminales de la bd
"""
def mostrar_nombre_terminal():
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_terminal, nombre_terminal FROM Terminal")

        #fetchone()
        return cursor.fetchall()

    except:
        print("Saliendo error en la base mostrar_nombre_terminal")
        exit(0)
    finally:
        desConectarBD(conn)
    return False

"""
busca una terminal por nombre en la bd
"""
def mostrar_nombre_terminal_unico(nombre_terminal):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_terminal, nombre_terminal FROM Terminal")

        #fetchone()
        for nombre in cursor.fetchall():
            if nombre_terminal == nombre[1]:
                return True, [nombre[0], nombre[1]]

    except:
        print("Saliendo error en la base mostrar_nombre_terminal_unico")
        exit(0)
    finally:
        desConectarBD(conn)
    return False,[]

"""
verifica que el nombre de la ruta no exista
"""
def verificar_nombre_ruta(nombre_ruta):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre_ruta FROM Ruta")

        #fetchone()
        for nombre in cursor.fetchall():
            if nombre_ruta == nombre[0]:
                return True
    except:
        print("Saliendo error en la base verificar_nombre_ruta")
        exit(0)
    finally:
        desConectarBD(conn)
    return False

"""
registra una ruta en la bd
"""
def registrar_ruta_BD(nombre_ruta, id_usuario, cantidad_pasajeros, camino):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Ruta (nombre_ruta, fk_id_usuario, cantidad_pasajeros, camino) VALUES (%s, %s, %s, %s)",
        (nombre_ruta, id_usuario, cantidad_pasajeros, camino))
    except:
        print("Saliendo error en la base registrar_ruta_BD")
        exit(0)
    finally:
        desConectarBD(conn)

"""
busca una ruta por nombre
"""
def buscar_datos_Ruta(nombre_ruta):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_ruta, nombre_ruta FROM Ruta")
        #fetchone()
        for nombre in cursor.fetchall():
            if nombre_ruta == nombre[1]:
                return True, [nombre[0], nombre[1]]

    except:
        print("Saliendo error en la base buscar_datos_Ruta")
        exit(0)
    finally:
        desConectarBD(conn)
    return False,[]

"""
registra un camino en la bd
"""
def registrar_camino_BD(posicion, id_ruta, id_terminal):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Camino (posicion, fk_id_ruta, fk_id_terminal) VALUES (%s, %s, %s)",
        (posicion, id_ruta, id_terminal))
    except:
        print("Saliendo error en la base registrar_camino_BD")
        exit(0)
    finally:
        desConectarBD(conn)

"""
muestra las rutas de la bd
"""
def mostrar_datos_ruta():
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_ruta, nombre_ruta FROM Ruta")

        #fetchone()
        nombres = []
        for nombre in cursor.fetchall():
            nombres.append(nombre)
        return nombres

    except:
        print("Saliendo error en la base mostrar_datos_ruta")
        exit(0)
    finally:
        desConectarBD(conn)
    return False,[]

"""
verifica que exista un venta
"""
def verificar_venta_ruta(id_ruta):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT fk_id_ruta FROM Venta")

        #fetchone()

        for id in cursor.fetchall():
            if id[0] == id_ruta:
                return True

    except:
        print("Saliendo error en la base verificar_venta_ruta")
        exit(0)
    finally:
        desConectarBD(conn)
    return False

"""
borra de la bd un camino por la ruta
"""
def borrar_Camino_por_id_Ruta(id_ruta):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Camino WHERE fk_id_ruta = %s", (id_ruta))

    except:
        print("Saliendo error en la base borrar_Camino_por_id_Ruta")
        exit(0)
    finally:
        desConectarBD(conn)

"""
borra una ruta de la bd por el id de la ruta
"""
def borrar_Ruta_por_id_ruta(id_ruta):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Ruta WHERE pk_id_ruta = %s", (id_ruta))

    except:
        print("Saliendo error en la base borrar_Ruta_por_id_ruta")
        exit(0)
    finally:
        desConectarBD(conn)

"""
muestra todos los datos de una terminal
"""
def mostrar_datos_Terminal():
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_terminal, nombre_terminal, fk_id_usuario FROM Terminal")

        #fetchone()
        nombres = []
        for nombre in cursor.fetchall():
            nombres.append(nombre)
        return nombres

    except:
        print("Saliendo error en la base mostrar_datos_Terminal()")
        exit(0)
    finally:
        desConectarBD(conn)
    return []

"""
verifica las terminales que hay en la tabla camino por el id de la terminal
"""
def verificar_terminales_en_Camino(id_terminal):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_camino, posicion, fk_id_ruta, fk_id_terminal FROM Camino WHERE fk_id_terminal = %s", (id_terminal))

        #fetchone()

        for id in cursor.fetchall():
            return True

    except:
        print("Saliendo error en la base verificar_terminales_en_Camino")
        exit(0)
    finally:
        desConectarBD(conn)
    return False

"""
borra una terminal por su id
"""
def borrar_Terminal_por_id_terminal(id_terminal):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Terminal WHERE pk_id_terminal = %s", (id_terminal))

    except:
        print("Saliendo error en la base borrar_Terminal_por_id_terminal")
        exit(0)
    finally:
        desConectarBD(conn)

"""
obtiene los datos de las rutas de la bd
"""
def obtener_datos_Ruta(terminal_1, terminal_2):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_ruta, nombre_ruta, cantidad_pasajeros, camino FROM Ruta")

        #fetchone()
        datos_ruta = []
        for rut in cursor.fetchall():
            lista_terminales = rut[3].split(",")
            existe_ruta = False
            i = 0
            while i < len(lista_terminales):

                if terminal_1 == lista_terminales[i]:
                    i = i +1
                    break
                i = i +1

            while i < len(lista_terminales):
                if terminal_2 == lista_terminales[i]:
                    existe_ruta = True
                    datos_ruta.append(rut)
                    i = i + 1
                    break
                i = i + 1

        return datos_ruta

    except:
        print("Saliendo error en la base obtener_datos_Ruta")
        exit(0)
    finally:
        desConectarBD(conn)
    return []

"""
obtenemos las ventas por el id de la ruta
"""
def obtener_Ventas(id_ruta):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_venta, fk_id_ruta, cantidad_pasajeros FROM Venta WHERE fk_id_ruta=%s", (id_ruta))

        #fetchone()
        datos_ruta = []
        for ven in cursor.fetchall():
            datos_ruta.append(ven)
        return datos_ruta

    except:
        print("Saliendo error en la base obtener_Ventas")
        exit(0)
    finally:
        desConectarBD(conn)
    return []


"""
se validan terminales por su id
"""
def validar_terminales_Ruta(terminal_1):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_terminal FROM Terminal WHERE nombre_terminal = %s", (terminal_1))

        #fetchone()
        for rut in cursor.fetchall():
            return True, rut[0]

    except:
        print("Saliendo error en la base validar_terminales_Ruta")
        exit(0)
    finally:
        desConectarBD(conn)
    return False, []

"""
se registra una venta
"""
def registrar_Venta_BD(id_usuario, fk_id_terminal_1, fk_id_terminal_2, fk_id_ruta, cantidad_pasajeros):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Venta (fk_id_usuario, fk_id_terminal_1, fk_id_terminal_2, fk_id_ruta, cantidad_pasajeros) VALUES (%s, %s, %s, %s, %s)",
        (id_usuario, fk_id_terminal_1, fk_id_terminal_2, fk_id_ruta, cantidad_pasajeros))
    except:
        print("Saliendo error en la base registrar_Venta_BD")
        exit(0)
    finally:
        desConectarBD(conn)

"""
se obtiene el id de la ultima venta
"""
def obtener_id_ultima_Venta_BD():
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(pk_id_venta) FROM Venta;")
        #fetchone()
        reg = 0
        for rut in cursor.fetchall():
            reg = rut[0]
            return reg

    except:
        print("Saliendo error en la base obtener_id_ultima_Venta_BD()")
        exit(0)
    finally:
        desConectarBD(conn)
    return -1

"""
inserta un boleta en la bd
"""
def insertar_Boleto_BD(id_venta, idem_boleto):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Boleto (fk_id_venta, idemtificacion_boleto) VALUES (%s, %s)",
        (id_venta, idem_boleto))
    except:
        print("Saliendo error en la base insertar_Boleto_BD")
        exit(0)
    finally:
        desConectarBD(conn)

"""
obtiene todas las rutas de la bd
"""
def obtener_todas_Rutas_BD():
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_ruta, nombre_ruta, cantidad_pasajeros, camino FROM Ruta")
        #fetchone()
        lista_val = []
        for rut in cursor.fetchall():
            lista_val.append(rut)
        return lista_val

    except:
        print("Saliendo error en la base obtener_todas_Rutas_BD")
        exit(0)
    finally:
        desConectarBD(conn)
    return []

"""
validar boletos por la bd
"""
def validar_Boleto_BD(id_boleto):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT pk_id_boleto, fk_id_venta FROM Boleto WHERE idemtificacion_boleto = %s", (id_boleto))

        #fetchone()
        for rut in cursor.fetchall():
            return True, rut[0], rut[1]

    except:
        print("Saliendo error en la base validar_Boleto_BD")
        exit(0)
    finally:
        desConectarBD(conn)
    return False, -1, -1

"""
borrar boleto por el id
"""
def borrar_Boleto(id_boleto):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Boleto WHERE pk_id_boleto = %s", (id_boleto))

    except:
        print("Saliendo error en la base borrar_boleto")
        exit(0)
    finally:
        desConectarBD(conn)

"""
obtener boletos vendidos por el id venta
"""
def obtener_boletos_vendido_Venta_BD(id_venta):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT cantidad_pasajeros FROM Venta WHERE pk_id_venta = %s", (id_venta))

        #fetchone()
        for rut in cursor.fetchall():
            return True, rut[0]

    except:
        print("Saliendo error en la obtener_boletos_vendido_Venta_BD")
        exit(0)
    finally:
        desConectarBD(conn)
    return False, -1

"""
se actualiza una venta por su id
"""
def actualizar_venta(id_venta, val_boleto):
    conn = conectarBD()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE Venta SET cantidad_pasajeros= %s WHERE pk_id_venta= %s", (val_boleto, id_venta))

    except:
        print("Saliendo error en la actualizar_venta")
        exit(0)
    finally:
        desConectarBD(conn)

"""
las funcines que tendra un vendedor
"""
def funciones_vendedores(nombre_vendedor, id_vendedor):
    entro = True
    while entro :
        cadena = input("1)Hacer venta\n2)Cancelar venta\n3)Salir\n")
        if cadena == "1":
            print("Hacer venta")
            """
            se hace una venta solicitando terminales o boletos
            """
            paradas_rutas = input("1)Terminales\n2)Rutas\n")
            if paradas_rutas == "1":

                """
                solicita numero de boletos
                """
                num_boletos = input("\nCantidad boletos:\n")
                vuelve = False
                esNum = True
                while esNum:
                    if vuelve :
                        num_boletos = input("\nCantidad boletos:\n")
                    try:
                        num_boletos = int(num_boletos)
                        if num_boletos == 0:
                            vuelve = True
                        else:
                            esNum = False
                    except:
                        print("No es un numero")
                        num_boletos = input("\nCantidad boletos:\n")

                """
                solicita primera y segunda parada
                """
                primera_parada = input("Primera parada\n")
                segunda_parada = input("Segunda parada\n")
                while primera_parada == segunda_parada:
                    segunda_parada = input("Segunda parada\n")
                validar_nombre_terminal1 = validar_terminales_Ruta(primera_parada)
                validar_nombre_terminal2 = validar_terminales_Ruta(segunda_parada)
                """
                si existen las paradas
                """
                if validar_nombre_terminal1[0] and validar_nombre_terminal2[0]:
                    """
                    mostramos las lineas disponibles
                    """
                    k = 0
                    arr_lin_con_asientos = []
                    print("\nEstas lineas estan disponibles: \n")

                    datos_ruta = obtener_datos_Ruta(primera_parada, segunda_parada)
                    for lin in datos_ruta:

                        """
                        validamos que haya suficientes boletos
                        """
                        can_pasa = 0
                        ventas_por_id = obtener_Ventas(lin[0])

                        for ven in ventas_por_id:
                            can_pasa = ven[2]+can_pasa

                        if can_pasa < lin[2]:
                            total = can_pasa + num_boletos
                            if total <= lin[2]:

                                print(str(k)+")"+lin[1])
                                k = k + 1
                                arr_lin_con_asientos.append(lin)

                    """
                    selecciona la ruta
                    """
                    indice_linea = input("\nIndice seleccionado:\n")
                    vuelve = False
                    esNum = True
                    while esNum:
                        if vuelve :
                            indice_linea = input("\nIndice seleccionado:\n")
                        try:
                            indice_linea = int(indice_linea)
                            if indice_linea >= len(arr_lin_con_asientos):
                                vuelve = True
                            else:
                                esNum = False
                        except:
                            print("No es un numero")
                            indice_linea = input("\Indice seleccionado:\n")

                    """
                    obtenemos valores para regustrar la venta
                    """
                    ind_vend = id_vendedor
                    c_pasajeros = num_boletos
                    term_1 = validar_nombre_terminal1[1]
                    term_2 = validar_nombre_terminal2[1]
                    id_ruta = arr_lin_con_asientos[indice_linea][0]

                    registrar_Venta_BD(ind_vend, term_1, term_2, id_ruta, c_pasajeros)
                    ult_id = obtener_id_ultima_Venta_BD()

                    """
                    creamos los boletos y los guardamos
                    """
                    print("Id del los boletos:")
                    j = 0
                    while j<int(c_pasajeros):
                        millis = int(round(time.time() * 1000))
                        print(millis)
                        insertar_Boleto_BD(ult_id, str(millis))
                        j = j + 1
                    print("\n")

                else:
                    print("No estan")

            elif paradas_rutas == "2":
                print("OPCION RUTAS\n")

                """
                solicitamos los boletos
                """
                num_boletos = input("\nCantidad boletos:\n")
                vuelve = False
                esNum = True
                while esNum:
                    if vuelve :
                        num_boletos = input("\nCantidad boletos:\n")
                    try:
                        num_boletos = int(num_boletos)
                        if num_boletos == 0:
                            vuelve = True
                        else:
                            esNum = False
                    except:
                        print("No es un numero")
                        num_boletos = input("\nCantidad boletos:\n")

                """
                obtenemos las rutas
                """
                lista_rutas_aceptadas = []
                lista_rutas = obtener_todas_Rutas_BD()
                for rut in lista_rutas:
                    """
                    validamos que haya espacio en las lineas
                    """
                    sum_ventas = 0;
                    list_ven = obtener_Ventas(rut[0])
                    for ven in list_ven:
                        sum_ventas = sum_ventas + ven[2]
                    sum_ventas = sum_ventas  + num_boletos
                    if sum_ventas <= rut[2]:
                        lista_rutas_aceptadas.append(rut)

                """
                mostramos las rutas disponibles
                """
                print("Estas rutas estan disponibles")
                k = 0
                while k < len(lista_rutas_aceptadas):
                    print(str(k)+")"+lista_rutas_aceptadas[k][1])
                    k = k + 1

                """
                selccionamos la ruta
                """
                indice_ruta = input("\nSelecciona un indice:\n")
                vuelve = False
                esNum = True
                while esNum:
                    if vuelve :
                        indice_ruta = input("\nSelecciona un indice:\n")
                    try:
                        indice_ruta = int(indice_ruta)
                        if indice_ruta >= len(lista_rutas_aceptadas):
                            vuelve = True
                        else:
                            esNum = False
                    except:
                        print("No es un numero")
                        indice_ruta = input("\nSelecciona un indice:\n")

                print("La ruta seleccionada es: "+ lista_rutas_aceptadas[indice_ruta][1])
                """
                obtenemos los valores para crear la ruta
                """
                id_use = id_vendedor
                #(7, 'linea 6', 9, 'olivos,zapotitlan')
                ruta = lista_rutas_aceptadas[indice_ruta][3]
                cam_seg = ruta.split(",")
                term_1 = cam_seg[0]
                term_2 = cam_seg[len(cam_seg)-1]
                val_term_1 =  validar_terminales_Ruta(term_1)
                val_term_2 =  validar_terminales_Ruta(term_2)
                id_term_1 = val_term_1[1]
                id_term_2 = val_term_2[1]
                id_ruta = lista_rutas_aceptadas[indice_ruta][0]
                c_pasajeros = num_boletos

                """
                se registra la venta
                """
                registrar_Venta_BD(id_use, id_term_1, id_term_2, id_ruta, c_pasajeros)
                ult_id = obtener_id_ultima_Venta_BD()


                """
                se ingresan los boletos
                """
                print("Id del los boletos:")
                j = 0
                while j<int(c_pasajeros):
                    millis = int(round(time.time() * 1000))
                    print(millis)
                    insertar_Boleto_BD(ult_id, str(millis))
                    j = j + 1
                print("\n")

        elif cadena == "2":

            """
            obtenemos el idem del boleto
            """
            id_boleto = input("\nCancelar boleto\nProporciona el id del boleto:\n")
            vuelve = False
            esNum = True
            while esNum:
                if vuelve :
                    id_boleto = input("\nCancelar boleto\nProporciona el id del boleto:\n")
                try:
                    id_boleto = int(id_boleto)
                    esNum = False
                except:
                    print("No es un numero")
                    id_boleto = input("\nCancelar boleto\nProporciona el id del boleto:\n")
            """
            eliminamos el boleto y añadimos un boleto mas para vender
            """
            valores_boleto = validar_Boleto_BD(id_boleto)
            if valores_boleto[0]:
                borrar_Boleto(valores_boleto[1])
                #True cantidad_pasajeros
                val_vendidos = obtener_boletos_vendido_Venta_BD(valores_boleto[2])
                bol_vendidos = val_vendidos[1]
                bol_vendidos = bol_vendidos - 1
                actualizar_venta(valores_boleto[2], bol_vendidos)
                print("Boleto cancelado")

        elif cadena == "3":
            print("Salir")
            entro = False
        else :
            print("Entrada incorrecta")

"""
funcines del Administrador
"""
def funciones_administrador(nombre_administrador, id_administrador):
    entra = True
    while entra:
        cadena = input("1)Crear nueva parada\n2)Crear nueva ruta\n3)Eliminar ruta\n4)Eliminar parada\n5)Salir\n")
        if cadena == "1":
            """
            obtenemos el nombre de la terminal y lo guardamos en la bd si no existe
            """
            print("crear nueva parada\n")
            nombre_terminal = input("Nombre de la terminal\n\n")
            existe_terminal = verificar_nombre_terminal(nombre_terminal)
            if not existe_terminal:
                registrar_terminal_BD(nombre_terminal, id_administrador)
                print("\n\nTerminal correctamente añadida\n\n")
            else:
                print("Existe la terminal\n")

        elif cadena == "2":
            """
            se muestra todas las rutas
            """
            print("crear nueva ruta\n")
            terminales = mostrar_nombre_terminal()
            for terminal in terminales:
                print(terminal[1])
            """
            solicitamos el numero de terminales que tendra la ruta
            """
            numTerminales = input("\nNumero de terminales que tendra la ruta:\n")
            vuelve = False
            esNum = True
            while esNum:
                if vuelve :
                    numTerminales = input("\nNumero de terminales que tendra la ruta:\n")
                try:
                    numTerminales = int(numTerminales)
                    if numTerminales == 0:
                        vuelve = True
                    else:
                        esNum = False
                except:
                    print("No es un numero")
                    numTerminales = input("\nNumero de terminales que tendra la ruta:\n")

            """
            validamos que existan suficientes terminales
            """
            while (int(numTerminales) > len(terminales)) or len(terminales)==0:
                numTerminales = input("\nNumero de terminal mayor al numero existete de terminales\nDar nuevamente el "
                +"numero de terminales que tendra la ruta\n")
            terminales_ruta = []#terminales que va tener la ruta formato [[3, 'nopalera'], [5, 'zapata'], [4, 'olivos']]
            """
            solicitamos el nombre de las terminales, que existan y que no se repitan
            """
            i = 0
            while i < int(numTerminales):
                nombreTerminal = input("\nNombre de la terminal\n")
                datos_terminal_unica = mostrar_nombre_terminal_unico(nombreTerminal)
                while not datos_terminal_unica[0]:
                    nombre_terminal = input("\nNombre de la terminal\n")
                    datos_terminal_unica = mostrar_nombre_terminal_unico(nombre_terminal)

                aceptado = True
                for termi in terminales_ruta:
                    if termi[1] == datos_terminal_unica[1][1]:
                        aceptado = False

                if aceptado :
                    terminales_ruta.append(datos_terminal_unica[1])
                    i = i + 1

            if len(terminales)>0:
                """
                solicitamos nombre de la ruta y verifica que no exista
                """
                nombre_de_la_ruta = input("\nNombre de la ruta\n")
                validacion = verificar_nombre_ruta(nombre_de_la_ruta)
                while validacion:
                    print("Ya existe esta ruta, pon otro nombre")
                    nombre_de_la_ruta = input("\nNombre de la ruta\n")
                    validacion = verificar_nombre_ruta(nombre_de_la_ruta)

                """
                solicitamos la cantidad maxima de pasajeros
                """
                cantidad_maxima_pasajeros = input("\nCantidad maxima pasajeros\n\n")
                camino = ""
                for term in terminales_ruta:
                    camino = camino + term[1]+","
                camino = camino[:-1]
                """
                guardamos en la bd la ruta y el camino
                """
                registrar_ruta_BD(nombre_de_la_ruta, id_administrador, cantidad_maxima_pasajeros, camino)

                datos_busqueda = buscar_datos_Ruta(nombre_de_la_ruta)
                if datos_busqueda[0]:
                    i = 0
                    while int(i) < len(terminales_ruta):
                        registrar_camino_BD(str(i), str(datos_busqueda[1][0]), str(terminales_ruta[i][0]))
                        i = i + 1

        elif cadena == "3":
            print("eliminar ruta")
            """
            mostramos todas las rutas
            """
            datos_ruta = mostrar_datos_ruta()
            for rutas in datos_ruta:
                print(rutas[1])

            """
            obtenemos el nombre de la ruta y validamos que no haya boletos vendidos
            """
            ruta_borrar = input("\nNombre de la ruta a borrar\n\n")
            borrado = False
            for rutas in datos_ruta:
                if rutas[1] == ruta_borrar:

                    if not verificar_venta_ruta(rutas[0]):
                        print("Se va a borrar el indice "+str(rutas[1]))
                        borrar_Camino_por_id_Ruta(rutas[0])
                        borrar_Ruta_por_id_ruta(rutas[0])
                        borrado = True
                    else :
                        print("Hay un boleto vendido en esa ruta")
            if borrado:
                print("Borrado existo")
            else :
                print("Borrado no existo")


        elif cadena == "4":
            """
            obtenemos el nombre de la parada y validamos que no haya una ruta con esta parada
            """
            print("eliminar parada")
            terminales = mostrar_datos_Terminal()
            for listado_terminales in terminales:
                print(listado_terminales[1])
            terminal_borrar = input("\nNombre de la terminal a borrar\n\n")
            borrado = False
            for listado_terminales in terminales:
                if listado_terminales[1] == terminal_borrar:

                    if not verificar_terminales_en_Camino(listado_terminales[0]):
                        print("Borrar terminal "+listado_terminales[1])
                        borrar_Terminal_por_id_terminal(listado_terminales[0])
                        borrado = True
                    else :
                        print("No se puede borrar terminal "+listado_terminales[1])

            if borrado:
                print("Terminal borrada")
            else:
                print("Terminal no borrada")

        elif cadena == "5" :
            """
            saliendo
            """
            entra = False
        else:
            print("error en entrada\n")


"""
funcion que registra un usuario
"""
def ingreso_registro():
    entro = True
    while entro:
        print("Sistema de transporte")
        """
        menu para ingresa, registrar o salir
        """
        cadena = input("1)Ingresar\n2)Registrar\n3)Salir\n")
        if cadena == "1":
            nombre_usuario = input("Nombre de usuario:\n")
            """
            solicitamos el nombre, verificamos que exista y entramos
            """
            verificar_usuario = verificar_nombre_usuarios(nombre_usuario)
            verificacion = verificar_usuario[0]
            if verificacion :
                if verificar_usuario[1] == 1:
                    print("Administrador")
                    funciones_administrador(nombre_usuario, verificar_usuario[2])
                else:
                    print("Vendedor")
                    funciones_vendedores(nombre_usuario, verificar_usuario[2])

            else :
                print("no entra")
        elif cadena == "2":
            """
            """
            """solicitamos el nombre del nuevo usuario y le pedimos un perfil y lo guardamos en la bd
            """
            nombre_usuario = input("Nombre de usuario nuevo:\n")
            id_perfil = input("Perfil de registro\n1)Administrador\n2)Vendedor\n")
            verificacion = verificar_nombre_usuarios(nombre_usuario)[0]
            if verificacion :
                print("existe")
            else :
                print("no existe")
                if id_perfil == "1" or id_perfil == "2":
                    registar_usuario_BD(nombre_usuario, id_perfil)
                else :
                    print("perfil incorrecto")
        elif cadena == "3":
            print("saliendo...")
            exit(0)




"""
main 
"""
if __name__ == '__main__':
    ingreso_registro()

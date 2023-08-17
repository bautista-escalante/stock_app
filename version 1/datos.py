import sqlite3

def crear_tabla():
    with sqlite3.connect("stock.db") as conexion:
                #### crear la tabla ####
        try:
            sentencia = ''' create table stock
                (
                id integer primary key autoincrement,
                cantidad real,
                categoria TEXT ,
                elemento TEXT,
                precio_alquiler real,
                precio_reposicion real
                )
                ''' 
            conexion.execute(sentencia)
            print("Se creo la tabla stock")
        except sqlite3.OperationalError:
            print("La tabla stock ya existe")

def agregar_datos(cantidad,categoria,elemento,precio_alquiler,precio_reposicion):
    with sqlite3.connect("stock.db") as conexion:
        try:
            sentencia = '''INSERT INTO stock (cantidad, categoria, elemento, precio_alquiler, precio_reposicion)
                        VALUES (?, ?, ?, ?, ?)'''
            datos = (cantidad, categoria, elemento, precio_alquiler, precio_reposicion)
            conexion.execute(sentencia, datos)
            print("Se agregaron los datos a la tabla stock")
        except sqlite3.Error:
            print("Error al agregar datos")

def actualizar_cantidad(elemento:str,cantidad:int)->int:
        with sqlite3.connect("stock.db") as conexion:
            try:
                # consegir la cantidad actual 
                lista = mostrar_elemento(elemento) 
                cantidad_actual= lista[1] + cantidad 
                # Actualizar la cantidad en la base de datos
                sentencia_update = '''UPDATE stock SET cantidad = ? WHERE elemento = ?'''
                conexion.execute(sentencia_update, (cantidad_actual, elemento))
                conexion.commit()
            except sqlite3.Error:
                print("Error al actualizar")

def actualizar_precios(categoria:str,inflacion:float):
    # consegir los precios actuales 
    lista = mostrar_categoria(categoria) 
    for datos in lista:
        precio_alquiler = datos[4] + (datos[4] * inflacion )
        precio_reposicion = datos[5] + (datos[5] * inflacion )
        try:
            with sqlite3.connect("stock.db")as conexion:
                # Actualizar la cantidad en la base de datos
                sentencia_update = '''UPDATE stock SET precio_alquiler=?,precio_reposicion=? WHERE categoria=?'''
                conexion.execute(sentencia_update, (precio_alquiler,precio_reposicion, categoria))
                conexion.commit()
        except sqlite3.Error as e:
            print("error inesperado",e)

def mostrar_elemento(elemento:str)->list:
    """rettorna una lista con los datos del elemnto que se pasa por parametro"""
    with sqlite3.connect("stock.db") as conexion: 
        try: 
            cursor = conexion.execute("SELECT * FROM stock WHERE elemento=?", (elemento,))
            datos = cursor.fetchall()
            datos=datos[0]
            print(datos)
            return datos
        except Exception:
            print("Error")

def mostrar_categoria(categoria):
    """retorna una tupla de listas"""
    with sqlite3.connect("stock.db") as conexion: 
        try: 
            #### imprimir en pantalla #### 
            cursor = conexion.execute("SELECT * FROM stock WHERE categoria = ?", (categoria,))
            datos = cursor.fetchall()
            return datos
        except Exception as e:
            print("Error",e)
#Importa librearia SQLITE3 para la creación de la base de datos
import sqlite3

 #Inicializa la creación de la bd y de los datos precargados
def inicializar_db(db_name = 'test.db'):
    #Crea la variable de conexión con la base de datos
    conn = sqlite3.connect(db_name) 
     #activa la seguridad y consistencia en los datos
    conn.execute("PRAGMA foreign_keys = ON;")
    #crea cursor 
    cursor = conn.cursor()

    #crea tabla con la variable query_create
    query_create_usuarios = """
    CREATE TABLE if not exists USUARIOS
    (
    id_user INTEGER PRIMARY KEY,
    user_nombre TEXT NOT NULL,
    user_apellido TEXT NOT NULL,
    DNI INT NOT NULL
    )
    """
    query_create_cuentas = """
    CREATE TABLE if not exists CUENTAS
    (
    id_cuentas INTEGER PRIMARY KEY,
    id_user INTEGER,
    FOREIGN KEY (id_user) REFERENCES USUARIOS(id_user)
    )
    """
    query_create_billeteras = """
    CREATE TABLE if not exists BILLETERAS
    (
    id_billetera INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo_billetera REAL NOT NULL,
    id_cuentas INTEGER,
    FOREIGN KEY (id_cuentas) REFERENCES CUENTAS(id_cuentas)
    )
    """
    query_create_movimientos = """
    CREATE TABLE if not exists MOVIMIENTOS
    (
    id_movimiento INTEGER PRIMARY KEY,
    tipo_movimiento TEXT,
    monto_movimiento REAL,
    id_cuentas INTEGER,
    FOREIGN KEY (id_cuentas) REFERENCES CUENTAS(id_cuentas)
    )
    """
    #consulta de ingresos de datos en las tablas
    query_ing_data_usuarios = """
    INSERT OR IGNORE INTO USUARIOS (id_user, user_nombre, user_apellido, DNI) VALUES (?,?,?,?)
    """

    query_ing_data_cuentas= """
    INSERT OR IGNORE INTO CUENTAS (id_cuentas, id_user) VALUES (?,?)
    """

    query_ing_data_billeteras= """
    INSERT OR IGNORE INTO BILLETERAS (id_billetera, saldo_billetera,id_cuentas) VALUES (?,?,?)
    """

    #lista de datos precargados
    precargados_usuarios = [(1007,"Alvaro","Retamoso",37000000), (1008,"José", "Pérez", 38000000), (2006,"María", "Garcia", 40000000), (2007, "Filomena", "Lopéz", 39000000)]
    precargados_cuentas = [(86,1007), (65,1008), (14,2006),(88,2007)]
    precargados_billeteras = [(9845, 874239.32 ,86), (3613, 134000,65),(9203, 134.40,14), (4498, 34623.30,88)]


    #ejecuta creacion tabla usuarios 
    conn.execute(query_create_usuarios)
    #ejecuta creacion tabla cuentas 
    conn.execute(query_create_cuentas)
    #ejecuta creacion tabla billeteras 
    conn.execute(query_create_billeteras)
    #ejecuta creacion tabla movimientos 
    conn.execute(query_create_movimientos)
    #ejecuta ingreso de datos precargados a tabla usuarios / cuentas / billeteras
    cursor.executemany(query_ing_data_usuarios,precargados_usuarios)
    cursor.executemany(query_ing_data_cuentas,precargados_cuentas)
    cursor.executemany(query_ing_data_billeteras,precargados_billeteras)

    #guarda en la bd
    conn.commit()
    #cierra la bd
    conn.close()

###### CONSULTAS A LA BASE DE DATOS UNA FUNCION POR CONSULTA #####

#Consulta seleccionar información (nombre, apellido, dni) tabla usuario según ID
def consulta_info_usuario(id_busca, db_name = 'test.db'):
    conn = sqlite3.connect(db_name) #Con esto creo la conexion a la bd
    conn.execute("PRAGMA foreign_keys = ON;") #con conto activo la seguridad e integridad de los datos
    #crea cursor 
    cursor = conn.cursor()
    query =  """
    SELECT * from USUARIOS WHERE id_user = ?
    """
    cursor.execute(query, (id_busca,)) #la funcion execute siempre necesita aqui recibir una tupla por eso va la coma en id_busca eso le dice que es una tupla
    resultado = cursor.fetchone()
    conn.close()
    return resultado

#Consulta numero de cuenta segun id_user
def consulta_nro_cuenta(id_busca, db_name = 'test.db'):
    conn = sqlite3.connect(db_name) #Con esto creo la conexion a la bd
    conn.execute("PRAGMA foreign_keys = ON;") #con conto activo la seguridad e integridad de los datos
    #crea cursor 
    cursor = conn.cursor()
    query =  """
    SELECT id_cuentas from CUENTAS where id_user = ?
    """
    cursor.execute(query, (id_busca,)) #la funcion execute siempre necesita aqui recibir una tupla por eso va la coma en id_busca eso le dice que es una tupla
    resultado = cursor.fetchone()
    conn.close()
    return resultado

#consulta movimientos de saldo en la cueta
def consulta_mostrar_movimientos (id_busca, db_name = 'test.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    query = """
    SELECT * from MOVIMIENTOS where id_cuentas = ?
    """
    cursor.execute(query, (id_busca,)) 
    resultado = cursor.fetchall()
    conn.close()
    return resultado

#Consulta de actualizar saldo en las billeteras
def consulta_actualizar_saldo(monto_actualizar, id_busca, db_name = 'test.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    query = """
    UPDATE BILLETERAS set saldo_billetera = ? where id_cuentas = (SELECT id_cuentas from CUENTAS where id_user = ? )
    """
    resultado = cursor.execute(query, (monto_actualizar, id_busca))
    conn.commit()
    conn.close()
    return resultado

#consulta que ingresa registro de movimiento a la billetera
def consulta_ingresa_movimiento(tipo_movimiento, monto_movimiento, id_cuentas, db_name = 'test.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    query = """
    INSERT INTO MOVIMIENTOS (tipo_movimiento, monto_movimiento, id_cuentas) VALUES (?,?,?)
    """
    resultado = cursor.execute(query, (tipo_movimiento, monto_movimiento, id_cuentas)) 
    conn.commit()
    conn.close()
    return resultado
 
#consulta saldo en la billetera
def consulta_saldo_billetera(id_busca, db_name = 'test.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    query = """
    SELECT saldo_billetera FROM BILLETERAS WHERE id_cuentas = (SELECT id_cuentas from CUENTAS where id_user = ?)
    """
    cursor.execute(query, (id_busca,)) 
    resultado = cursor.fetchone()
    conn.close()
    return resultado

 #consulta id_billetera
def consulta_id_billetera(id_busca, db_name = 'test.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    query = """
    SELECT id_billetera FROM BILLETERAS WHERE id_cuentas = (SELECT id_cuentas from CUENTAS where id_user = ?)
    """
    cursor.execute(query, (id_busca,)) 
    resultado = cursor.fetchone()
    conn.close()
    return resultado

#Consulta información de usuario a partir del numero de billeter
def consulta_info_cuenta_x_billetera(db_name = 'test.db'):
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    query ="""
    SELECT user_nombre, user_apellido from Usuarios Where (id_cuentas = ?)
    """
    resultado = cursor.execute(query) 
    conn.commit()
    conn.close()
    return resultado





import pytest
import sqlite3
import os
import db_manager

# FIXTURE
@pytest.fixture
def db_provisoria():
    """Crea una base de datos física para el test y la limpia al terminar"""
    nombre_db = "db_para_testear.db"
    
    # 1. Inicializa la base de datos
    db_manager.inicializar_db(db_name=nombre_db)
    
    yield nombre_db # Entrega el nombre de la base al test
    
    # 2. Borra los archivos temporales al finalzar
    if os.path.exists(nombre_db):
        os.remove(nombre_db)

# 1: Verificar que los Usuarios se cargaron bien 
def test_usuarios_precargados(db_provisoria):
    res = db_manager.consulta_info_usuario(1007, db_name=db_provisoria)
    assert res is not None
    assert res[1] == "Alvaro"
    assert res[2] == "Retamoso"

# 2: Probar Actualización de Saldo
def test_actualizacion_saldo(db_provisoria):
    id_user = 1007
    nuevo_saldo = 9999.99
    db_manager.consulta_actualizar_saldo(nuevo_saldo, id_user, db_name=db_provisoria)
    res_saldo = db_manager.consulta_saldo_billetera(id_user, db_name=db_provisoria)
    assert res_saldo[0] == 9999.99

# 3: Probar Vínculo de Cuenta 
def test_obtener_nro_cuenta(db_provisoria):
    res = db_manager.consulta_nro_cuenta(1007, db_name=db_provisoria)
    assert res[0] == 86

#4: Probar Registro de Movimientos
def test_ingreso_y_lectura_movimientos(db_provisoria):
    id_cuenta = 86
    db_manager.consulta_ingresa_movimiento("Prueba Test", 100.0, id_cuenta, db_name=db_provisoria)
    movs = db_manager.consulta_mostrar_movimientos(id_cuenta, db_name=db_provisoria)
    assert any(m[1] == "Prueba Test" and m[2] == 100.0 for m in movs)

#5: Probar Consulta de Billetera 
def test_id_billetera(db_provisoria):
    res = db_manager.consulta_id_billetera(1007, db_name=db_provisoria)
    assert res[0] == 9845
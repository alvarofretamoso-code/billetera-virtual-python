from models import Usuario, Cuenta, Billetera, Movimientos
def test_usuario_metodos_formato():
    # Arrange: crea USUARIO
    user = Usuario(1007, "Alvaro", "Retamoso", 37000000)

    # Act: ejecuta los métodos de la clase usuario
    res_datos = user.datos_usuario()
    res_envio = user.datos_usuario_p_envio()
    res_nombre = user.datos_usuario_nombre_y_apellido()

    # Assert: verifica el formato por separado
    assert res_datos == "Usuario Seleccionado: Alvaro Retamoso - DNI:37000000"
    assert "enviará dinero a la cuenta de Alvaro Retamoso" in res_envio
    assert res_nombre == "Alvaro Retamoso"

def test_billetera_mostrar_saldo():
    # Arrange
    mi_billetera = Billetera(9845, 1500.50, 86)

    # Act
    resultado = mi_billetera.mostrar_saldo()

    # Assert
    assert resultado == "Su saldo es de 1500.5"

def test_movimientos_formato():
    # Arrange
    mov = Movimientos(1, "Extracción", -500.0, 86)

    # Act
    resultado = mov.mostrar_movimientos()

    # Assert
    assert resultado == "Extracción -500.0"

def test_cuenta_creacion():
    # Arrange: define los ID
    id_cuenta_esperado = 86
    id_usuario_esperado = 1007

    # Act: instancia la clase
    cuenta = Cuenta(id_cuenta_esperado, id_usuario_esperado)

    # Assert: Verificamos que los datos se guardaron donde corresponde
    assert cuenta.id_cuentas == 86
    assert cuenta.id_user == 1007
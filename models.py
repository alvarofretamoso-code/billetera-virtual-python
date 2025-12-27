#definicion de la clase Usuarios:
class Usuario:
    def __init__ (self, id_user, user_nombre, user_apellido, DNI):
        self.id_user = id_user
        self.user_nombre = user_nombre
        self.user_apellido = user_apellido
        self.DNI = DNI
    def datos_usuario(self):
        return f"Usuario Seleccionado: {self.user_nombre} {self.user_apellido} - DNI:{self.DNI}"
    def datos_usuario_p_envio(self):
        return f"Usted enviará dinero a la cuenta de {self.user_nombre} {self.user_apellido} - DNI:{self.DNI}"
    def datos_usuario_nombre_y_apellido(self):
        return f"{self.user_nombre} {self.user_apellido}"
        
#definicion de la clase CUENTA:
class Cuenta:
    def __init__ (self, id_cuentas, id_user):
        self.id_cuentas = id_cuentas
        self.id_user = id_user

#definicion de la clase billetera    
class Billetera:
    def __init__ (self, id_billetera, saldo_billetera, id_cuentas):
        self.id_billetera = id_billetera
        self.saldo_billetera = saldo_billetera
        self.id_cuentas = id_cuentas

    def mostrar_saldo (self):
        return f"Su saldo es de {self.saldo_billetera}"

#definicion de la clase movimientos
class Movimientos:
    def __init__ (self, id_movimiento, tipo_movimiento, monto_movimiento, id_cuentas):
        self.id_movimiento = id_movimiento
        self.tipo_movimiento = tipo_movimiento
        self.monto_movimiento = monto_movimiento
        self.id_cuentas = id_cuentas

    def mostrar_movimientos (self):
        return f"{self.tipo_movimiento} {self.monto_movimiento}"

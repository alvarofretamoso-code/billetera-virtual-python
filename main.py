#Import
from unicodedata import bidirectional
import db_manager
import sys
#importa  modelos
from models import Movimientos
from models import Billetera
from models import Usuario
#Inicializa base de datos
db_manager.inicializar_db()
#ID válidos para selección de datos precargados
id_validos = [1,2,3,4]
id_seleccionado = 0
#función de selección de usuarios
def sel_us():
    while True:
        try:
            eleccion = int(input("¿Con la billetera de quien queres trabajar? 1: ALVARO / 2: JOSE / 3: FILOMENA / 4: MARIA : "))
            if eleccion in id_validos:
                if eleccion == 1:
                    return db_manager.consulta_info_usuario(1007)
                elif eleccion ==2:
                    return db_manager.consulta_info_usuario(1008)
                elif eleccion ==3:
                    return db_manager.consulta_info_usuario(2006)
                elif eleccion ==4:
                    return db_manager.consulta_info_usuario(2007)
            else:
                print ("Elija una opción correcta.")
                return (sel_us())
        except ValueError:
                print ("Ingrese un valor númerico.")


#función de selección de dinero
def sel_destinatario():
    while True:
        try:
            eleccion = int(input("¿A quién desea enviar dinero? 1: ALVARO / 2: JOSE / 3: FILOMENA / 4: MARIA : "))
            if eleccion in id_validos:
                if eleccion == 1:
                    return db_manager.consulta_info_usuario(1007)
                elif eleccion ==2:
                    return db_manager.consulta_info_usuario(1008)
                elif eleccion ==3:
                    return db_manager.consulta_info_usuario(2006)
                elif eleccion ==4:
                    return db_manager.consulta_info_usuario(2007)
            else:
                print ("Elija una opción correcta.")
                return (sel_destinatario())
        except ValueError:
            print ("Ingrese un valor númerico")


#convierte la selección de usuario a la variable us_sel
us_sel = sel_us()
#carga los datos de la consulta a los atributos la clase usuario
us1 = Usuario(us_sel[0],us_sel[1],us_sel[2],us_sel[3])
#llama la funcion de mostrar datos del usuario de la clase usuario
print (us1.datos_usuario())
#convierte el ID del usuario seleccinado a la varibale id_seleccionado
id_seleccionado = us_sel[0]

#función menú de seleción para usuario
def menu():
    while True:
        print ("¿Qué deseas hacer?: ")
        print ("1. Ver Saldo. ")
        print ("2. Ingresar Dinero. ")
        print ("3. Enviar Dinero.")
        print ("4. Extraer Dinero.")
        print ("5. Ver mis movimientos.")
        print ("6. Salir.")
        try:
            elegi = int(input("Elegí: "))
            
            #opción 1
            if elegi == 1:
                id_cuenta = db_manager.consulta_nro_cuenta(id_seleccionado)
                id_cuenta_conv = id_cuenta[0]
                id_billetera2 = db_manager.consulta_id_billetera(id_cuenta[0])
                consulta_saldo_sql = db_manager.consulta_saldo_billetera(id_seleccionado)
                most_sal = Billetera( id_billetera2, consulta_saldo_sql[0], id_cuenta)
                saldo_final = print (most_sal.mostrar_saldo())
                convertido = int(consulta_saldo_sql[0])

                #opción 1.1
                while True:
                    print ("¿Qué deseas hacer?: ")
                    print ("1. Extraer Dinero. ")
                    print ("2. Ingresar Dinero. ")
                    print ("3. Enviar Dinero. ")
                    print ("4. Ver movimientos de mi cuenta. ")
                    print ("5. Salir")
                    try: 
                        elegi2 = int(input("Elegí: "))
                        
                        if elegi2 == 1:
                            print ("¿Cuánto dinero va a extraer?: ")
                            try:
                                extraccion = int(input("Ingrese monto: "))
                                if extraccion < convertido:
                                    print(f"¿Extraer {extraccion}?: ").lower()
                                    while True:
                                        confirma = input("[SI] [NO]: ").lower()
                                        if confirma == "si":
                                            resta = convertido - extraccion
                                            actualiza_saldo = db_manager.consulta_actualizar_saldo(resta, id_seleccionado)
                                            db_manager.consulta_ingresa_movimiento("Extracción", -extraccion, id_cuenta_conv )
                                            print (f"Extracción existosa.")
                                            print (f"Su Saldo es de {resta}")
                                            break
                                        elif confirma == "no":
                                            print ("Extracción cancelada")
                                            break
                                        else:
                                            print ("Por favor ingrese SI o NO")

                                else:
                                    print ("Saldo insuficiente, ingrese un monto menor.")
                            except:
                                print ("Ingrese un valor númerico.") 
                                continue


                        #opción 1.2
                        elif elegi2 == 2:
                            print ("¿Cuánto dinero va a ingresar?: ")
                            try:
                                ingreso = int(input("Ingrese monto: "))
                                if ingreso > 0:
                                    print(f"Ingresar $ {ingreso} a su cuenta?: ")
                                    saldo_usuario_2 = db_manager.consulta_saldo_billetera(id_seleccionado)
                                    saldo_usuario_convertido_2 = int(saldo_usuario_2[0])
                                    while True:
                                        confirma = input("[SI] [NO]: ").lower()
                                        if confirma == "si":
                                            aumento = saldo_usuario_convertido_2 + ingreso
                                            actualiza_saldo_aumento = db_manager.consulta_actualizar_saldo(aumento, id_seleccionado)
                                            db_manager.consulta_ingresa_movimiento("Ingreso", ingreso, id_cuenta_conv )
                                            print (f"Ingreso Exitoso")
                                            print (f"Su Saldo es de {aumento}")
                                            break
                                        elif confirma == "no":
                                            print ("Ingreso cancelado.")
                                            break
                                        else:
                                            print ("Por favor ingrese SI o NO")
                                            
                                else:
                                    print ("Ingrese un monto mayor")
                            except:
                                print ("Ingrese un valor númerico.") 
                                

                        #opción 1.3
                        elif elegi2 == 3:
                            destinatario = sel_destinatario()
                            if destinatario != us_sel:
                                info_destinatario = Usuario(destinatario[0],destinatario[1],destinatario[2],destinatario[3])
                                print (f"¿Cuánto dinero le enviaras a {info_destinatario.datos_usuario_nombre_y_apellido()}?")
                                while True:
                                    try:
                                        monto =  int(input("Ingrese un monto: "))
                                        saldo_usuario = db_manager.consulta_saldo_billetera(id_seleccionado)
                                        saldo_usuario_convertido = int(saldo_usuario[0])
                                        if monto <= saldo_usuario_convertido:
                                            print (f"¿Enviar {monto} a {info_destinatario.datos_usuario_nombre_y_apellido()}?")
                                            while True:
                                                eleccion = (input("[SI] [NO]: ")).lower()
                                                if eleccion == "si":
                                                    saldo_receptor = db_manager.consulta_saldo_billetera(destinatario[0])
                                                    saldo_receptor_conve = int(saldo_receptor[0]) 
                                                    total_a_restar_a_emite =  saldo_usuario_convertido - monto
                                                    total_sumar = saldo_receptor_conve + monto
                                                    db_manager.consulta_ingresa_movimiento("Transferencia a otra cuenta", monto, id_cuenta_conv )
                                                    db_manager.consulta_actualizar_saldo(total_sumar, destinatario[0])
                                                    db_manager.consulta_actualizar_saldo(total_a_restar_a_emite, id_seleccionado)
                                                    saldo_usuario_final = db_manager.consulta_saldo_billetera(id_seleccionado)
                                                    saldo_usuario_f_convertido = int(saldo_usuario_final[0])
                                                    print ("¡Dinero Enviado!")
                                                    print (f"Su saldo es de ${saldo_usuario_f_convertido}")
                                                    break
                                                
                                                elif eleccion == "no":
                                                    print ("Transferencia Cancelada")
                                                    break
                                                    
                                                else:
                                                     print ("Por favor ingrese SI o NO")
                                            break        
                                        else:
                                            print ("Saldo insufienciente. Ingrese un monto menor")
                                             
                                    except ValueError:
                                        print ("Ingrese un valor ico")
                            else:
                                print ("No podes enviarte dinero a vos mismo")
                    
                        #opción 1.4
                        elif elegi2 == 4:
                            user_movimientos = db_manager.consulta_mostrar_movimientos(id_cuenta_conv)
                            for fila in user_movimientos:
                                mov = Movimientos(fila[0], fila[1], fila[2], fila[3])
                                print(mov.mostrar_movimientos())

                        #opcion 1.5
                        elif elegi2 == 5:
                            print ("¡Chau!")
                            sys.exit()
                    except ValueError:
                        print ("Ingrese un valor númerico.")     
            #opción 2  
            elif elegi == 2:
                print ("¿Cuánto dinero va a ingresar?: ")
                while True:
                    try:
                        ingreso = int(input("Ingrese monto: "))
                        if ingreso > 0:
                            print(f"Ingresar $ {ingreso} a su cuenta?: ")
                            saldo_usuario_2 = db_manager.consulta_saldo_billetera(id_seleccionado)
                            saldo_usuario_convertido_2 = int(saldo_usuario_2[0])
                            while True:
                                confirma = input("[SI] [NO]: ").lower()
                                if confirma == "si":
                                    id_cuenta_op2 = db_manager.consulta_nro_cuenta(id_seleccionado)
                                    id_cuenta_conv_op2 = id_cuenta_op2[0]
                                    aumento = saldo_usuario_convertido_2 + ingreso
                                    actualiza_saldo_aumento = db_manager.consulta_actualizar_saldo(aumento, id_seleccionado)
                                    db_manager.consulta_ingresa_movimiento("Ingreso", ingreso, id_cuenta_conv_op2 )
                                    print (f"¡Ingreso Exitoso!")
                                    print (f"Su Saldo es de {aumento}")
                                    break
                                    print (menu())
                                elif confirma == "no":
                                    print ("Ingreso cancelado.")
                                    break
                                else:
                                    print ("Ingrese SI o NO")
                                    
                        break
                    except ValueError:
                        print ("Ingrese un valor númerico")

            #opción 3
            elif elegi == 3:
                destinatario = sel_destinatario()
                if destinatario != us_sel:
                    info_destinatario = Usuario(destinatario[0],destinatario[1],destinatario[2],destinatario[3])
                    print (f"¿Cuánto dinero le enviaras a {info_destinatario.datos_usuario_nombre_y_apellido()}?")
                    while True:
                        try:
                            monto =  int(input("Ingrese un monto: "))
                            saldo_usuario = db_manager.consulta_saldo_billetera(id_seleccionado)
                            saldo_usuario_convertido = int(saldo_usuario[0])
                            if monto <= saldo_usuario_convertido:
                                print (f"¿Enviar {monto} a {info_destinatario.datos_usuario_nombre_y_apellido()}?")
                                while True:
                                    eleccion = (input("[SI] [NO]: ")).lower()
                                    if eleccion == "si":
                                        id_cuenta_op3 = db_manager.consulta_nro_cuenta(id_seleccionado)
                                        id_cuenta_conv_op3 = id_cuenta_op3[0]
                                        saldo_receptor = db_manager.consulta_saldo_billetera(destinatario[0])
                                        saldo_receptor_conve = int(saldo_receptor[0]) 
                                        total_a_restar_a_emite =  saldo_usuario_convertido - monto
                                        total_sumar = saldo_receptor_conve + monto
                                        db_manager.consulta_ingresa_movimiento("Transferencia a otra cuenta", monto, id_cuenta_conv_op3 )
                                        db_manager.consulta_actualizar_saldo(total_sumar, destinatario[0])
                                        db_manager.consulta_actualizar_saldo(total_a_restar_a_emite, id_seleccionado)
                                        saldo_usuario_final = db_manager.consulta_saldo_billetera(id_seleccionado)
                                        saldo_usuario_f_convertido = int(saldo_usuario_final[0])
                                        print ("¡Dinero Enviado!")
                                        print (f"Su saldo es de ${saldo_usuario_f_convertido}")
                                        break
                                        print (menu())

                                    elif eleccion == "no":
                                        print ("Transferencia cancelada.")
                                        break
                            
                                    else:
                                        print ("Ingrese SI o NO")

                            else:
                                print ("Saldo insufienciente. Ingrese un monto menor")
                            break
                            
                        except ValueError:
                            print ("Ingrese un valor númerico")     
                else:
                    print ("No podes enviarte dinero a vos mismo")

            #opcion 4
            elif elegi == 4:
                print ("¿Cuánto dinero va a extraer?: ")
                try:
                    extraccion = int(input("Ingrese monto: "))
                    consulta_saldo_sql = db_manager.consulta_saldo_billetera(id_seleccionado)
                    convertido2 = int(consulta_saldo_sql[0])
                    if extraccion < convertido2:
                        print(f"¿Extraer {extraccion}?: ")
                        while True:
                            confirma = input("[SI] [NO]: ").lower()
                            if confirma == "si":
                                id_cuenta_op4 = db_manager.consulta_nro_cuenta(id_seleccionado)
                                id_cuenta_conv_op4 = id_cuenta_op4[0]
                                resta = convertido2 - extraccion
                                actualiza_saldo = db_manager.consulta_actualizar_saldo(resta, id_seleccionado)
                                db_manager.consulta_ingresa_movimiento("Extracción", -extraccion, id_cuenta_conv_op4 )
                                print (f"Extracción existosa.")
                                print (f"Su Saldo es de {resta}")
                                print (menu())
                            elif confirma == "no":
                                print ("Extracción cancelada")
                                break
                            else:
                                print ("Ingrese SI o NO")
                            
                    else:
                        print ("Saldo insuficiente, ingrese un monto menor.")       
                except ValueError:
                    print ("Ingrese un valor númerico")

            #opcion 5
            elif elegi == 5:
                id_cuenta2 = db_manager.consulta_nro_cuenta(id_seleccionado)
                id_cuenta_conv2 = id_cuenta2[0]
                user_movimientos = db_manager.consulta_mostrar_movimientos(id_cuenta_conv2)
                for fila in user_movimientos:
                    mov = Movimientos(fila[0], fila[1], fila[2], fila[3])
                    print(mov.mostrar_movimientos())

            if elegi == 6:
                print ("¡Chau!")
                sys.exit()
        except ValueError:
            print ("Ingrese un valor númerico.")

#inicializa menú
menu()



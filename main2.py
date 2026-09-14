import os

os.system("cls")

# 2. Cajero automático con restricciones
# Crear un programa que simule un cajero automático.
# El usuario comienza con un saldo definido por el programa.
# Debe poder realizar operaciones:

# Para retirar dinero se deben cumplir estas condiciones:
# •	El monto debe ser positivo.
# •	No puede superar el saldo disponible.
# •	Solo se permiten retiros múltiplos de $10.000.
# •	El usuario puede realizar como máximo 3 retiros.
# •	Si intenta retirar dinero sin saldo suficiente, debe mostrar un mensaje apropiado.
# El menú debe continuar apareciendo hasta que el usuario seleccione salir.
# Desafío lógico
# ¿Qué debería ocurrir si el usuario escribe "hola" cuando el programa espera una opción numérica?

print("=== CAJERO AUTOMÁTICO ===")
saldo = 0
cantidad_retiro = 0
opcion = 0
deposito = 0
while opcion != 4:
    print("1.	Consultar saldo")
    print("2.	Depositar dinero")
    print("3.	Retirar dinero")
    print("4.	Salir")
    try:
        opcion = int(input("Ingrese opción:\n"))
        if opcion == 1:
            print("1.	Consultar saldo")
            print(f"Saldo actual: ${saldo}")
        elif opcion == 2:
            print("2.	Depositar dinero")
            while deposito <= 0:
                deposito = int(input("Ingrese valor a depositar\n"))
                if deposito <= 0:
                    print("El deposito debe se mayor a 0")
            saldo = saldo + deposito
        elif opcion == 3:
            print("3.	Retirar dinero")
            if saldo <= 0:
                print("No tienes suficiente saldo para retirar")
            else:
                while cantidad_retiro < 3:
                    retiro = int(input("Ingrese el monto del retiro\n"))
                    if retiro > saldo:
                        print("No se efectuo el retiro")
                    else:
                        saldo = saldo - retiro
                        print(f"retiro exitoso, saldo: {saldo}")
                        cantidad_retiro = cantidad_retiro + 1
                    seguir = int(input("¿Desea realizar otro retiro? 1.si 2.no\n"))
                    if seguir == 2:
                        break
        elif opcion == 4:
            print("4.	Salir")
    except:
        print("Opción debe ser valor numérico")

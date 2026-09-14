import os

os.system("cls")

# Python básico: pensamiento lógico
# Objetivo
# Resolver problemas utilizando exclusivamente conceptos fundamentales de Python:
# Recomendación: antes de programar, que cada alumno escriba en papel las reglas del problema, los datos que necesita, las condiciones y el flujo de decisiones.
# 1. Sistema de clasificación de una competencia
# Una competencia tiene varias pruebas. Cada participante obtiene un puntaje entre 0 y 100 en tres pruebas:
# •	Velocidad
# •	Precisión
# •	Resistencia
# El puntaje final se calcula de la siguiente manera:
# •	Velocidad representa el 30%.
# •	Precisión representa el 40%.
# •	Resistencia representa el 30%.
# La clasificación depende del resultado final:
# •	90 o más: Excelente
# •	75 a 89: Muy bueno
# •	60 a 74: Aprobado
# •	Menos de 60: No aprobado
# Pero existen dos condiciones especiales:
# •	Si alguna prueba obtiene menos de 40 puntos, el participante queda automáticamente No aprobado.
# •	Si las tres pruebas son superiores a 95, debe aparecer además el mensaje "Rendimiento excepcional".
# Desafío adicional
# El programa debe solicitar los puntajes y validar que estén entre 0 y 100.
# Si el usuario introduce algo que no sea un número, el programa no debe finalizar con error.

print("=== CLASIFICACIÓN DE COMPETENCIA ===")
try:
    velocidad = float(input("Puntaje de velocidad:\n"))
    precision = float(input("Puntaje de precisión:\n"))
    resistencia = float(input("Puntaje de resistencia:\n"))

    if (
        velocidad < 9
        or velocidad > 100
        or precision < 0
        or precision > 100
        or resistencia < 0
        or resistencia > 100
    ):
        print("ERROR: los puntajes deben estar en el rango 0 a 100")
    else:
        puntaje_final = velocidad * 0.30 + precision * 0.40 + resistencia * 0.30
        print(f"Puntaje final: {puntaje_final}")

        if velocidad < 40 or precision < 40 or resistencia < 40:
            print("CLASIFICACIÓN: No Aprobado")
        elif puntaje_final >= 90:
            print("CLASIFICACIÓN: Excelente")
        elif puntaje_final >= 75:
            print("CLASIFICACIÓN: Muy Bueno")
        elif puntaje_final >= 60:
            print("CLASIFICACIÓN: Aprobado")
        else:
            print("CLASIFICACIÓN: No Aprobado")

        if velocidad > 95 and precision > 95 and resistencia > 95:
            print("Rendimiento Excepcional")


except:
    print("Los valores deben ser numéricos")

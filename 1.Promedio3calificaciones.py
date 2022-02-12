Calificación_1 = float(input("Escribe la califiacion1"))
Calificación_2 = float(input("Escribe la califiacion2"))
Calificación_3 = float(input("Escribe la califiacion3"))


promedio = (Calificación_1 + Calificación_2 + Calificación_3) / 3

print("promedio " + str(promedio))

if (promedio >= 6):
    print("aprobado")
else:
    print("reprobado")
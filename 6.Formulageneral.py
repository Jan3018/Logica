from math import sqrt

print("Calcular los valores de X1 y X2 con la formula general")

A = float(input("Dame el valor de A: "))
B = float(input("Dame el valor de B: "))
C = float(input("Dame el valor de C: "))

x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)

print("X1: " + str(x1))
print("X2: " + str(x2))
#Tienen 31 días: Enero, marzo, mayo, julio, agosto, octubre y diciembre.
#Tienen 30 días: Abril, junio, septiembre y noviembre.
#Tienen 28 días: Febrero.

print("Para calcular tu pago, favor de ingresar los datos siguientes: ")
print("Mes: \n1.-31 días: Enero, marzo, mayo, julio, agosto, octubre y diciembre \n2.-28 días: Febrero \n3.-30 días: Abril, junio, septiembre y noviembre")

respuesta_mes = int (input("Elige el numero de los días laborados para calcular tu nómina"))
salario_diario = float(input("Escribe tu sueldo diario: "))
iva_trasladado = 0.16
iva_retenido = 0.106666
isr_retenido = 0.10
sueldo_30dias = ((salario_diario*30)*(1+iva_trasladado))-(((salario_diario*30)*iva_retenido)+((salario_diario*30)*isr_retenido))
sueldo_31dias = ((salario_diario*31)*(1+iva_trasladado))-(((salario_diario*30)*iva_retenido)+((salario_diario*30)*isr_retenido))
sueldo_28dias = ((salario_diario*28)*(1+iva_trasladado))-(((salario_diario*30)*iva_retenido)+((salario_diario*30)*isr_retenido))

if ( respuesta_mes == 1):
    print("Tu sueldo real será de : " + str(sueldo_31dias))
elif ( respuesta_mes == 2 ):
   print("Tu sueldo real será de : " + str(sueldo_28dias))
else:
    print("Tu sueldo real será de : " + str(sueldo_30dias))
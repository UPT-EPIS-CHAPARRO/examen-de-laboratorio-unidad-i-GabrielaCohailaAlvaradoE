# Mayor salario y numero de empleados
nempleados = int(input("Ingrese la cant. de empleados: "))

contador = 0 
for i in range (nempleados):
    salario = int(input("Ingrese su sueldo: "))

    mayor = salario 
    if salario > mayor :
        mayor = salario

    contador += 1

    if salario == 0 :
        break

print ("El numero de empleado es: ",contador)
print ("El mayor sueldo es: ",mayor)

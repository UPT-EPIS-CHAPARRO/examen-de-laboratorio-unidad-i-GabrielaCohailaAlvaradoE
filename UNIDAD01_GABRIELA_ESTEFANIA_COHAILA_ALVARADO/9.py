#Dados los valores de código de postulantes (string), nota1 (Número real) y nota2 (número real), calcular el promedio de las notas (nota1=60%, nota2=40%).

codigo_postulante = float(input("Ingrese el código del postulante: "))
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))

promedio = (nota1 * 0.6) + (nota2 * 0.4)

print(f"El promedio del postulante {codigo_postulante} es: {promedio:.2f}")

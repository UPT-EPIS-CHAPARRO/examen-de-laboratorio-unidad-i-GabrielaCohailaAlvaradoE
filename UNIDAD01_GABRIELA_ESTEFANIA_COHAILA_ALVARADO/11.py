n = int(input("Ingrese la cant. de numeros: "))

pares = 0
impares = 0
suma_p = 0
suma_i = 0

for i in range (0,n+1):
    if i%2 == 0 :
        suma_pares += 1
        pares += i
    else:
        suma_impares += 1
        impares	+= i

promedio_p = pares/suma_p
promedio_i = impares/suma_i

print ("Promedio de pares : ",promedio_p)
print ("Promedio de impares : ",promedio_i)
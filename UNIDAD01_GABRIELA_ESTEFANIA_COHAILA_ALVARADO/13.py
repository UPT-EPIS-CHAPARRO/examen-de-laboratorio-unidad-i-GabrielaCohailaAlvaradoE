#Facoriales de n, 
n = int(input("Ingrese el valor de n: "))

f = 1

for i in range (1,n+1):
    f *= i 
print ("El factorial de n es: ",f)
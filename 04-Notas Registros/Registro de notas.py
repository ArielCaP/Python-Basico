
cantidad_notas=int(input("Cuantas notas desea ingresar al sistema?🤔:"))
notas=[]
for i in range(cantidad_notas): #repite lo que sigue, una vez por cada número de esa secuencia, y en cada vuelta guarda el número actual en la variable i
    nota= float(input(f"Ingrese la nota #{i+1}: "))
    notas.append(nota)

promedio=sum(notas)/len(notas)
mas_alta=max(notas)
mas_baja=min(notas)


print(f"El promedio es: {promedio}\nLa nota mas alta es: {mas_alta}\nLa nota mas baja es: {mas_baja}")

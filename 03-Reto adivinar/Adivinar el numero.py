import random
numero_secreto= random.randint(1,100)
intentos=0 #contador que inicia en 0
while True: #Mientras esto sea cierto, epite lo que esta adentro
    intento= int(input("Adivina el numero del 1 al 100😎: "))
    intentos+=1
    if intento<numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    elif intento>numero_secreto:
        print("Muy alto, intenta de nuevo.")
    else:
        print(f"Felicidades!🎉Adivinaste el numero en {intentos} intentos.")
        break

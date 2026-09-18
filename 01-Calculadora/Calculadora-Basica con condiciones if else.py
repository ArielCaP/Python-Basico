# CALCULADORA: CODIGO BASICO CON IF,ELSEIF,ELSE E IF ANIDADO#
numero1= float(input("Ingrese el primer numero: "))
numero2= float(input("Ingrese el segundo numero: "))


operacion= input("¿Que operacion deseas hacer? (+, -, *, /): ")
#
if operacion == "+":
    resultado= numero1+numero2
    print(f"El reultado de la suma es:{resultado}😁")
elif operacion == "-":
    resultado= numero1-numero2
    print(f"El resultado de la resta es:{resultado}😃")
elif operacion == "*":
    resultado= numero1*numero2
    print(f"El resultado de la multiplicacion es:{resultado}😉")
elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir para cero ----ERROR----😪")
    else:
        resultado=numero1/numero2
        print(f"El resultado de la division es:{resultado}😆") 
else:
    print("error----")

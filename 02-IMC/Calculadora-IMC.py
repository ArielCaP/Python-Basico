#CACLULADORA IMC
estatura= float(input("Ingrese su estatura(m)😃: "))
peso= float(input("Ingrese su peso(Kg)😁: "))
IMC= peso/(estatura*estatura)
#CONDICIONES IF, ELSEIF, ELSE
if IMC < 18.5:
    print(f"El IMC {IMC} muestra que tiene bajo peso.")
elif IMC >= 18.5 and IMC <= 24.9:
    print(f"El IMC {IMC} muestra un peso normal.")
elif IMC >=25 and IMC <=29.9:
    print(f"El IMC {IMC} muestra sobrepeso.")
else:
    print(f"El IMC {IMC} muestra obesidad.")

#elif 18.5 <= IMC <= 24.9: tambien equivale al if q use antes

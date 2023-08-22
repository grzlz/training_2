## cuanto fue
## entre cuantos
## propina
def tipcalculator():
    cuenta = float(input("Hola, ¿Cuanto fue en total?: "))
    personas= float(input("¿Entre cuantos van a pagar?: "))
    pago_individual = cuenta/personas
    propina=float(input("¿Cuanto quieres dejar de propina (10,12,15,20)?: "))
    pago_final= round(pago_individual * (1+propina/100),2)
    print(f"Te toca pagar: ${pago_final}" ) 

tipcalculator() 

## cuanto fue
## entre cuantos
## propina
def tipcalculator():
    cuenta = float(input("Hola, ¿Cuanto fue en total?: "))
    personas= float(input("¿Entre cuantos van a pagar?: "))
    pago_individual = cuenta/personas
    propina=float(input("¿Cuanto quieres dejar de propina (10,12,15,20)?: "))
    pago_final= pago_individual * (1+propina/100)
    print(f"Te toca pagar: ${round(pago_final,2)}" ) 

tipcalculator() 

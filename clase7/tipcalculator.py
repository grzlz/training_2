## cuanto fue
## entre cuantos
## propina
def tipcalculator():
    cuenta = float(input("cuanto fue?: "))
    personas= float(input("Entre cuantos van a pagar?: "))
    pago_individual = cuenta/personas
    propina=float(input("Cuanto quieres dejar de propina(0,5,10,12,15,20?: "))
    pago_final= pago_individual * (1+propina/100)
    
    print(f"te toca pagar: {pago_final}" ) 

tipcalculator() 

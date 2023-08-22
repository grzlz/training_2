def TipCalculator():

    print("Hola, comiste chido?")
    total_cuenta = int(input("Cuanto fue el total?"))
    personas = int(input("Cuantas personas pagaran?"))
    pago = total_cuenta/personas
    propina = int(input("Cuanto dejaran de propina?"))
    pago_propina = round(pago*(1+(propina/100)))
    print(f"Debes pagar: ${pago_propina}")

TipCalculator()

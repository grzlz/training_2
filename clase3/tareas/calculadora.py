op = input("Qué operación quieres hacer (sumar,restar,multiplicar,dividir)?:  ")
print(op)
if op == "sumar":
    print("El usuario escogio sumar")
    num1= int(input("Dame el primer número: "))
    num2= int(input("Dame el segundo número: "))
    suma= num1 + num2
    print("El resultado de tu suma es:", suma)
elif op == "restar":
    print("El usuario escogio restar")
    num1= int(input("Dame el primer número: "))
    num2= int(input("Dame el segundo número: "))
    resta= num1 - num2
    print("El resultado de tu resta es:", resta)
elif op == "multiplicar":
    print("El usuario escogio multiplicar")
    num1= int(input("Dame el primer número: "))
    num2= int(input("Dame el segundo multiplicar: "))
    multiplicacion= num1 * num2
    print("El resultado de tu multiplicación es:", multiplicacion)
elif op == "dividir": 
    print("El usuario escogio dividir")
    num1= int(input("Dame el numerador: "))
    num2= int(input("Dame el denominador: "))
    division= num1 / num2
    print("El resultado de tu división es:", division)
    

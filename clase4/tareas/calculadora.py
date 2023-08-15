def calculadora():
      
    print("Hola bienvenido a la calculadora")
    op=input("Que operacion quieres ejecutar?(suma/resta/multiplicacion/division)")
    if op == "suma":
        primer_numero = int(input("dame tu primer numero"))
        segundo_numero = int(input("dame tu segundo numero"))
        print(f"tu numero es: {primer_numero + segundo_numero}")
    elif op == "resta":
        primer_numero = int(input("dame tu primer numero"))
        segundo_numero = int(input("dame tu segundo numero"))
        print(f"tu numero es: {primer_numero - segundo_numero}")
    elif op == "multiplicacion":
        primer_numero = int(input("dame tu primer numero"))
        segundo_numero = int(input("dame tu segundo numero"))
        print(f"tu numero es: {primer_numero * segundo_numero}")
    elif op == "division":
        primer_numero = int(input("dame tu primer numero"))
        segundo_numero =int(input("dame tu segundo numero"))
        print(f"tu numero es: {primer_numero / segundo_numero}")

       
calculadora()

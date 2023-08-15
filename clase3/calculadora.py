def calculadora():
    while True:
        print('Hola bienvenido a calculator2000')
        op=input('Que operacion quieres ejecutar?(suma/resta/mult/div/sumama) exit para salir')
        if op== "exit" :
            break
        print('Hasta luego!')
        if op == 'suma' : 
            print('El usuario escogio una suma')
            print('Que numeros quieres sumar?')
            x=eval(input('Cual es tu primer numero?'))
            y=eval(input('Cual es tu segundo numero?'))
            su=x+y
            print("El resultado es "+  str(su))
        elif op == 'resta':
            print('El usuario escogio una resta')
            print('Que numeros quieres restar?')
            x=eval(input('Cual es tu primer numero?'))
            y=eval(input('Cual es tu segundo numero?'))
            re=x-y
            print("El resultado es "+ " "+ str(re))
        elif op == 'sumama':
            arr=input('Numeros (divididos por commas sin espacios)')
            z=arr.split(',')
            print(z)
            for x in range(0,len(z)):
                z[x]=int(z[x])    
            print('El resultado es ' +str(sum(z)))
        elif op == 'mult':
            arr=input('Numeros (divididos por commas sin espacios)')
            z=arr.split(',')
            m=1
            for x in range(0,len(z)):
                z[x]=int(z[x])
                m=m*z[x]
            print('El resultado es ' +str(m))
        elif op == 'div':
            arr=input('Numeros (divididos por commas sin espacios)')
            z=arr.split(',')
            m=1
            for x in range(0,len(z)):
                z[x]=int(z[x])
                m=m/z[x]
            print('El resultado es ' +str(sum(z)))
        else:
            print('El usuario eligio otra operacion')
            
calculadora()
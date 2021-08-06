# calculadora-de-fisica-MRU-MRUV-CAIDAL-
este es un proyecto que me pidieron en clase de crear una calculadora fisica 
import math
opciones=['1','2','3','4','5','6','7','8','9','10','11','12']
while True:                 
    print('''seleccione la formuila que desea resolver:
    MRU
    1. velocidad:                     v=d/t
    2. Distancia:                     d=v*t
    3. Tiempo:                        t=d/v
    FORMULAS MRUV
    4. Aceleracion1:                  a=v7/t
    5. Aceleracion2:                  a=vf-vi/t
    6. Velocidad final:               vf=vi+a*t
    7. Velocidad incial:              vi=vf-a*t
    FORMULAS CAIDA LIBRE
    8.  V=Vo-G*T
    9.  V^2=Vo^2-2g*(D)")
    10. D=Vo*T-1/2G*T^2")
    11. D=((VoV)/2)*T
    12. Salir''')
    opcion=input('introduzca la formula a resolver')
    if not (opcion in opciones):
        print('no se seleciono alguna opcion valida')
        input('pulse enter para continuar')
        continue
    elif opcion=='1':
        try:
            valora=float(input('distancia(m)'))
            valorb=float(input('tiempo(s)'))
            valorc=valora/valorb
            print('la velocidad es:',round(valorc,2),'m/s')
            input('pulse para continuar')
        except :
            print('ha introducido valores incorrectos')
            continue
    elif opcion=='2':
        try:
            valora=float(input)
            valorb=float(input('tiempo(s)'))
            valorc=valora/valorb
            input('pulse para continuar')
        except:
            print('ha introducido valores incorectos')
            continue
    elif opcion=='3':
        try:
            valora=float(input('distancia(m):'))
            valorb=float(input('velocidad(m/s)'))
            valorc=valora/valorb
            print('el tiempo es:',round(valorc,2),'s')
            input('pulse enter para continuar')
        except :
            print('ha introducido valores incorrectos')
            continue
    elif opcion=='4':
        try:
            valora=float(input('distancia(m):'))
            valorb=float(input('velocidad(m/s)'))
            valorc=valora/valorb
            print('la aceleracion es:',round(valorc,2),'m/s^2')
            input('pulse enter para continuar')
        except :
            print('ha introducido valores incorrectos')
            continue
    elif opcion=='5':
        try:
            valora=float(input('velocidad final(m/s)'))
            valorb=float(input('velocidad inicial(m/s)'))
            valorc=float(input('tiempo(s)'))
            valord=(valora-valorb)/valorc
            print('la aceleracion es:',round(valord,2),'m/s^2')
        except :
            print('ha introducido un valor erroneo')
            continue
    elif opcion=='6':
        try:
            valora=float(input('velocidad incial(m/s)'))
            valorb=float(input('aceleracion(m/s^2)'))
            valorc=float(input('tiempo(s)'))
            valord=valora+(valorb*valorc)
            print('la veloidad final es:',round(valord,2),'m/s')
            input('pulse para continuar')
        except:
            print('ha introducido valores erroneos')
            continue
    elif opcion=='7':
        try:
            valora=float(input('velocidad incial(m/s)'))
            valorb=float(input('aceleracion(m/s^2)'))
            valorc=float(input('tiempo(s)'))
            valord=valora-(valorb*valorc)
            print("la velodicad inicial es:",round(valord,2),'m/s')
            input('pulse para continuar')
        except:
            print('ha introducido valores incorrectos')
            continue
    elif opcion=='8':
        try:
            valora=float(input('Ingrese la velocidad inicial:' ))
            valorb=float(input('Ingrese el tiempo: '))
            valorc=float(input('ingrese gravedad:'))
            valord=valora-valorc*valorb
            print ('La velocidad final es: ',round(valord,2))
            input('pulse para continuar')
        except:
            print('ha introducido valores erroneos')
            continue
    elif opcion=='9':
        try:
            valora=float(input('Ingrese la velocidad inicial: '))
            valorb=float(input('Ingrese la distancia recorrida: '))
            valorc=float(input('ingrese gravedad'))
            valord=math.sqrt(valora**2-2*valorc*valorb)
            print ('La velocidad final es: ',round(valord,2))
            input('pulse para continuar')
        except:
            print('ha introducido valores erroneos')
            continue
    elif opcion=='10':
        try:
            valora=float(input('Ingrese la velocidad inicial: '))
            valorb=float(input('Ingrese el tiempo: '))
            valorc=float(input('ingrese la gravedad:'))
            valord=valora*valorb+1/2*valorc*valorb*2
            print ('La distancia recorrida es: ',round(valord,3))
            input('pulse para continuar')
        except:
            print('ha introducido valores erroneos')
            continue
    elif opcion=='11':
        try:
            valora=input('Ingrese la velocidad inicial: ')
            valorb=input('Ingrese la velocidad final: ')
            valorc=input('Ingrese el tiempo: ')
            valord=(((valorb+valora)/2)*valorc)
            print ('La distancia recorrida es:',round(valord,2))
            input('pulse para continuar')
        except:
            print('ha introducido valores erroneos')
            continue
    elif opcion=='12':
        print('fin del programa')  
        break

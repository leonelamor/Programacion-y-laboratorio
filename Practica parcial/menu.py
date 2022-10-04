import main
import re
def app():
    almacenar=""
    while(True):
        print('''
        1-Listar los primeros N héroes.
        2-Ordenar y Listar héroes por altura. 
        3-Ordenar y Listar héroes por fuerza. 
        4-Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: menor o mayor) 
        5-Buscar héroes por inteligencia [good, average, high] 
        6-Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
        7- salir
        '''
        )
        respuesta=input(">")
        if(re.search("^[1-7]+$",respuesta)):
            if(respuesta=="1"):
                tope=input("Hasta que indice de la lista quiere mostrar?")
                if(re.search("^[0-9]+$",tope)):
                    tope=int(tope)
                    long=len(main.lista_personajes)
                    if(tope<long):
                        almacenar=main.func_mostrar(main.lista_personajes[:tope])
                    else:
                        print("Se excedio de indices")
                else: print("Dato invalido, debe ser un numero")

            elif(respuesta=="2"):
                dato=input("Digite (asc) si quiere ordenar los heroes por altura de forma ascendente, de lo contrario digite (desc)")
                dato=dato.lower()
                if(re.search("asc",dato) or re.search("desc",dato)):
                    
                    almacenar=main.func_mostrar(main.nahu_sort(main.lista_personajes,"altura",dato),"altura")
                else:
                    print("Opcion invalida. Tiene que ingresar asc o desc")

            elif(respuesta=="3"):
                dato=input("Digite (asc) si quiere ordenar los heroes por fuerza de forma ascendente, de lo contrario digite (desc)")
                dato=dato.lower()
                if(re.search("asc",dato) or re.search("desc",dato)):  
                        almacenar=main.func_mostrar(main.nahu_sort(main.lista_personajes,"fuerza",dato),"fuerza")
                else:
                    print("Opcion invalida. Tiene que ingresar asc o desc")

            elif(respuesta=="4"):
                key=input("Ingrese clave que quiere utilizar(fuerza)(altura)(peso)")
                key=key.lower()
                if(re.search("fuerza",key) or re.search("peso",key) or re.search("altura",key)):
                    elecc=input("Ingrese si quiere imprimir (mayores) o (menores) al promedio")
                    elecc=elecc.lower()
                    if(re.search("mayores",elecc) or re.search("menores", elecc)):
                        almacenar=main.func_mostrar(main.promedio(main.lista_personajes,key,elecc))
                    else:
                        print("Respuesta incorrecta, debe ingresar mayores o menores")
                else:
                    print("Respuesta incorrecta debe ingresar fuerza, peso o altura")


            elif(respuesta=="5"):
                inteligencia=input("Quiere filtrar por (average) (good) o (high)")
                inteligencia=inteligencia.lower()
                if(re.search("good",inteligencia)or re.search("average",inteligencia) or re.search("high", inteligencia)):
                    print(main.func_mostrar(main.heroes_por_inteligencia(main.lista_personajes,inteligencia),"inteligencia"))
                else:
                    print("Respuesta incorrecta debe ingresar good high o average")

            elif(respuesta=="6"):
                    main.guardar_archivo(almacenar)
            elif(respuesta=="7"):
                print("Salio del programa")
                break
        else:
            print("Opcion invalida, ingrese un numero del 1 al 7")

app()
 
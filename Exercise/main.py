from data_stark import lista_personajes
'''
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''

#--------- Ejercicio 1 ------
def superheroe_nombres():
    for superheroe in lista_personajes:
        print(superheroe["nombre"])
#---- Ejercicio 2 -----
def superheroe_nombres_y_alturas():
    for superheroe in lista_personajes:
        print(superheroe["nombre"],superheroe["altura"])

#---- Ejercicio 3 ----
def superheroe_altura_maxima():
    maximo_superheroe= lista_personajes[0]
    for superheroe in lista_personajes:
        if(float(superheroe["altura"])>float(maximo_superheroe["altura"])):
            maximo_superheroe=superheroe

    print(maximo_superheroe["altura"])
#---- Ejercicio 4----
def superheroe_altura_minima():
    minimo_superheroe= lista_personajes[0]
    for superheroe in lista_personajes:
        if(float(superheroe["altura"])<float(minimo_superheroe["altura"])):
            minimo_superheroe=superheroe

    print(minimo_superheroe["altura"])

#---- Ejercicio 5 ----
def promedio_superheroes():
    contador_superheroes=0
    acumulador_altura_superheroes=0

    for superheroe in lista_personajes:
        contador_superheroes+=1
        acumulador_altura_superheroes+=float(superheroe["altura"])
        
        
    promedio_altura=acumulador_altura_superheroes/contador_superheroes
    print(promedio_altura)

#---- Ejercicio 6 ----
def nombre_mas_y_menos_altura():
    maximo_superheroe= lista_personajes[0]
    for superheroe in lista_personajes:
        if(float(superheroe["altura"])>float(maximo_superheroe["altura"])):
            maximo_superheroe=superheroe
    minimo_superheroe= lista_personajes[0]
    for superheroe in lista_personajes:
        if(float(superheroe["altura"])<float(minimo_superheroe["altura"])):
            minimo_superheroe=superheroe


    print(minimo_superheroe["nombre"])
    print(maximo_superheroe["nombre"])

#---- Ejercicio 7 ----
def superheroe_mas_y_menos_pesado():
    superheroe_mas_pesado=lista_personajes[0]
    superheroe_menos_pesado=lista_personajes[0]

    for superheroe in lista_personajes:
        if(float(superheroe["peso"])>float(superheroe_mas_pesado["peso"])):
            superheroe_mas_pesado=superheroe
    for superheroe in lista_personajes:
        if(float(superheroe["peso"])<float(superheroe_menos_pesado["peso"])):
            superheroe_menos_pesado=superheroe

    print(superheroe_mas_pesado["nombre"])
    print(superheroe_menos_pesado["nombre"])

while (True):
    respuesta=input("Presione 1 para la lista de nombres de superherones\n Presione 2 para nombre y altura superheroe\n Presione 3 para el superheroe con altura maxima \n Presione 4 para el superheroe con altura minima \n Presione 5  para obtener el promedio de la altura  \n Presione 6 para para saber quien tiene menos y mas altura \n Presione 7 para  saber quien es mas y menos pesado\n Presione 8 para salir \n")
    if(respuesta=="1"):
        superheroe_nombres()
    elif(respuesta=="2"):
        superheroe_nombres_y_alturas()
    elif(respuesta=="3"):
        superheroe_altura_maxima
    elif(respuesta=="4"):
        superheroe_altura_minima
    elif(respuesta=="5"):
        promedio_superheroes()
    elif(respuesta=="6"):
        nombre_mas_y_menos_altura()
    elif(respuesta=="7"):
        superheroe_mas_y_menos_pesado()
    elif(respuesta=="8"):
        break


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
'''
#----Ejercicio A-----
for superheroe in lista_personajes:
    if(superheroe["genero"]=="M"):
        print(superheroe["nombre"])
#----Ejercicio B ----

for superheroe in lista_personajes:
    if(superheroe["genero"]=="F"):
        print(superheroe["nombre"])

'''

#--- Ejercicio C ---

def primer_masculino():
    for heroe in lista_personajes:
        if(heroe["genero"] == "M"):
            return heroe

def primer_femenino():
    for heroe in lista_personajes:
        if(heroe["genero"] == "F"):
            return heroe


def altura_maxima_hombre():
    altura_personaje_maxima=primer_masculino()
    altura_personaje_maxima["altura"]=float(altura_personaje_maxima["altura"])
    for superheroe in lista_personajes:
        if(superheroe["genero"]=="M"):
            superheroe["altura"]=float(superheroe["altura"])
            if(superheroe["altura"]>altura_personaje_maxima["altura"]):
                altura_personaje_maxima=superheroe
                nombre_mas_alto=superheroe["nombre"]

    return nombre_mas_alto


def altura_maxima_femenino():
    altura_personaje_maxima=primer_femenino()
    altura_personaje_maxima["altura"]=float(altura_personaje_maxima["altura"])
    for superheroe in lista_personajes:
        if(superheroe["genero"]=="F"):
            superheroe["altura"]=float(superheroe["altura"])
            if(superheroe["altura"]>altura_personaje_maxima["altura"]):
                altura_personaje_maxima=superheroe
                nombre_mas_alto=altura_personaje_maxima["nombre"]

    return nombre_mas_alto

def altura_minimo_hombre():
    altura_personaje_minimo=primer_masculino()
    altura_personaje_minimo["altura"]=float(altura_personaje_minimo["altura"])

    for superheroe in lista_personajes:
            superheroe["altura"]=float(superheroe["altura"])
            if(superheroe["altura"]<altura_personaje_minimo["altura"] and superheroe["genero"]=="M"):
                altura_personaje_minimo=superheroe

    return altura_personaje_minimo["nombre"]

def altura_minimo_mujer():
    altura_personaje_minimo=primer_femenino()
    altura_personaje_minimo["altura"]=float(altura_personaje_minimo["altura"])

    for superheroe in lista_personajes:
            superheroe["altura"]=float(superheroe["altura"])
            if(superheroe["altura"]<altura_personaje_minimo["altura"] and superheroe["genero"]=="F"):
                altura_personaje_minimo=superheroe

    return altura_personaje_minimo["nombre"]

def promedio_altura_hombres():
    contador_hombres=0
    acumulador_altura_hombres=0
    for superheroe in lista_personajes:
        if(superheroe["genero"]=="M"):
            contador_hombres+=1
            acumulador_altura_hombres+=float(superheroe["altura"])
        if(contador_hombres>0):
            promedio_altura=acumulador_altura_hombres/contador_hombres
        else:
            print("No hay hombres")
    return promedio_altura

def promedio_altura_mujeres():
    contador_mujeres=0
    acumulador_altura_mujeres=0
    for superheroe in lista_personajes:
        if(superheroe["genero"]=="F"):
            contador_mujeres+=1
            acumulador_altura_mujeres+=float(superheroe["altura"])
        if(contador_mujeres>0):
            promedio_altura=acumulador_altura_mujeres/contador_mujeres
        else:
            print("No hay mujeres")
    return promedio_altura
   
def informar_nombres():
    
    print("el superheroe hombre con altura maxima es: {0} - el superheroe femenino con altyura maxima es: {1} - el superheroe hombre con altura minima es: {2} - el superheroe mujer con altura minima es {3}".format(altura_maxima_hombre(), altura_maxima_femenino(), altura_minimo_hombre(), altura_minimo_mujer()))



def lista_heroes_color_ojos():
    lista_color_ojos=[]
    for color in lista_personajes:
        lista_color_ojos.append(color["color_ojos"])
    lista_seteada=set(lista_color_ojos)
    lista_colores=[]
    for color_ojos in lista_seteada:
        dic_color_ojos={}
        dic_color_ojos["Color"]=color_ojos
        dic_color_ojos["Cantidad"]=0

        for heroe in lista_personajes:
            if (color_ojos==heroe["color_ojos"]):
                dic_color_ojos["Cantidad"]+=1
        lista_colores.append(dic_color_ojos)

def lista_heroes_color_pelo():
    lista_color_pelo=[]
    for color in lista_personajes:
        lista_color_pelo.append(color["color_pelo"].lower())
    lista_seteada=set(lista_color_pelo)
    lista_color_pelo=[]
    for color_pelo in lista_seteada:
        dic_nuevo={}
        dic_nuevo["Color"]=color_pelo
        dic_nuevo["Cantidades"]=0
        
        for superheroe in lista_personajes:
            if (superheroe["color_pelo"].lower()== color_pelo):
                dic_nuevo["Cantidades"]+=1
        lista_color_pelo.append(dic_nuevo)
    print(lista_color_pelo)
            
lista_heroes_color_pelo()

    


    





    
  



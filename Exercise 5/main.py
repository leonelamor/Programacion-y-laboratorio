from cgitb import text
import json
import re
def imprimir_dato(heroes:str):
    print(heroes)


def imprimir_menu_desafio_5():
    mensaje=("A- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n B- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\nC- Recorrer la lista y determinar cuál es el superhéroe más alto de género M \nD- Recorrer la lista y determinar cuál es el superhéroe más alto de género F \nE- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M \nF-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F \nG- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M\nH Recorrer la lista y determinar la altura promedio de los  superhéroes de género \nI Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores \n J determinar cuántos superhéroes tienen cada tipo de color de ojos.\nK Determinar cuántos superhéroes tienen cada tipo de color de pelo.\nM Determinar cuántos superhéroes tienen cada tipo de inteligencia .\n N Listar todos los superhéroes agrupados por color de ojos.\nO Listar todos los superhéroes agrupados por color de pelo.\n Z Fin")
    imprimir_dato(mensaje)


def stark_menu_principal_desafio_5():
    imprimir_menu_desafio_5()
    respuesta=input("Ingrese una letra")
    respuesta=respuesta.upper()

    if(re.match("[A-Z]", respuesta)):
        return respuesta
    else:
        return -1



def stark_marvel_app_5(lista:list):
    while(True):
        respuesta=stark_menu_principal_desafio_5()
        if(respuesta=="A"):
            pass
        elif(respuesta=="B"):
            pass
        elif(respuesta=="C"):
            pass        
        elif(respuesta=="D"):
            pass
        elif(respuesta=="E"):
            pass
        elif(respuesta=="F"):
            pass
        elif(respuesta=="G"):
            pass
        elif(respuesta=="H"):
            pass
        elif(respuesta=="I"):
            pass
        elif(respuesta=="J"):
            pass
        elif(respuesta=="K"):
            pass
        elif(respuesta=="M"):
            pass
        elif(respuesta=="N"):
            pass
        elif(respuesta=="O"):
            pass
        elif(respuesta=="Z"):
            break


def leer_archivo(nombre_archivo:str):
    with open (nombre_archivo) as archivo:
        archivo= json.load(archivo)
        lista_heroes=archivo["heroes"]
        lista_heroes=list[dict](lista_heroes)
    return lista_heroes

lista_heroes=leer_archivo("Exercise 5\data_stark.json")


def guardar_archivo(nombre_archivo:str,texto:str):
    flag=False
    with open (nombre_archivo,"w+") as archivo:
        archivo.writelines(texto)
        flag=True
    if(flag==True):
        print("Se creó el archivo: {0}".format(nombre_archivo))
    else:
        print("Error al crear el archivo: {0}".format(nombre_archivo))
    return flag
    
def capitalizar_palabras(palabra:str):
    palabra=palabra.capitalize()
    return palabra

def obtener_nombre_capitalizado(dic_heroe:dict):
    nombre_capitalizado=capitalizar_palabras(dic_heroe["nombre"])
    return nombre_capitalizado


def obtener_nombre_y_dato(dic_heroe:dict,clave:str):
    nombre_capitalizado=obtener_nombre_capitalizado(dic_heroe)
    dato=dic_heroe[clave]
    mensaje="{0} | Fuerza: {1}".format(nombre_capitalizado,dato)
    return mensaje


def es_genero(dic_heroe:dict,sexo:str):
    if(dic_heroe["genero"]==sexo):
        return True
    else:
        return False
def stark_guardar_heroe_genero(lista:list,sexo:str):
    mensaje=""
    for heroe in lista:
        gen=es_genero(heroe,sexo)
        if(gen):
            nombre=obtener_nombre_capitalizado(heroe)
            mensaje+=nombre+","
            
    
    titulo_formateado="heroes_"+sexo
    mensaje = mensaje[:len(mensaje)-1]
    print(mensaje)

    return guardar_archivo(titulo_formateado,mensaje)

def calcular_min(lista:list,key:str):
    minimo=lista[0]
    for heroe in lista:
        if(minimo[key]<heroe[key]):
            minimo=heroe
    print(minimo[key])
    return minimo[key]

def calcular_max(lista:list,key:str):
    maximo=lista[0]
    for heroe in lista:
        if(maximo[key]>heroe[key]):
            maximo=heroe
    return maximo[key]

def calcular_min_genero(lista:list,genero:str,key:str):
    minimo_genero={}
    flag=False
    for heroe in lista:
        if(heroe["genero"]==genero and flag==False):
            minimo_genero=heroe
            flag=True
        if(heroe["genero"]==genero and minimo_genero[key]<heroe[key]):
            minimo_genero=heroe       

    return minimo_genero["nombre"]


def calcular_max_genero(lista:list,genero:str,key:str):
    maximo_genero={}
    flag=False
    for heroe in lista:
        if(heroe["genero"]==genero and flag==False):
            maximo_genero=heroe
            flag=True
        if(heroe["genero"]==genero and maximo_genero[key]>heroe[key]):
            maximo_genero=heroe       

    return maximo_genero["nombre"]
    

def calcular_max_min_dato(lista:list,genero:str,key:str,max_min):
    if(max_min=="maximo"):
        return calcular_max_genero(lista,genero,key)
    elif(max_min=="minimo"):
        return calcular_max_min_dato(lista,genero,key)


def buscar_heroe(lista,patron):
    lista_provisional=[]
    for elemento in lista:
        match=re.search(patron,elemento["color_ojos"],re.IGNORECASE)
        if(match):
            lista_provisional.append(elemento["nombre"])
    return lista_provisional

print(buscar_heroe(lista_heroes,"brown"))



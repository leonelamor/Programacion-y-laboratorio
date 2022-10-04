import json
import re
def cargar_json(ruta):
    with open (ruta,"r") as archivo:
        data=json.load(archivo)
        lista_personajes=data
        lista_personajes=lista_personajes["results"]
        lista_personajes=list[dict](lista_personajes)
    return lista_personajes
lista_personajes=cargar_json("PP_STARWARS\data.json")

def mostrar(lista,key="name"):
    mensaje=""
    for personaje in lista:
        mensaje+="El nombre es:{0} {1}{2}".format(personaje["name"],key,personaje[key])
    return mensaje

def max_min(lista_personajes,key,orden):
    minimo=0
    for elemento in lista_personajes:
        if (orden=="asc"):
            if(int(elemento[key])<int(elemento[key][minimo])):
                minimo=elemento
            return minimo



print(max_min(lista_personajes,"mass","asc"))

def nahuel_sort(lista_personajes,key,orden):
    lista_impresa=[]
    while (len(lista_personajes)>0):
        min=max_min(lista_personajes,key,orden)
        lista_impresa.append(lista_personajes.pop(min))
    return lista_impresa

def buscador_personajes(lista,personaje):
    for elemento in lista:
        match=re.search(personaje,lista,re.IGNORECASE)
        if(match):
            return elemento


def personaje_mas_alto(lista_personajes,genero):
    maximo=0
    flag=0
    for elemento in lista_personajes:
        if(elemento["gender"]==genero):
            if(int(elemento["height"])>maximo or flag==0):
                maximo=int(elemento["height"])
                elem_maximo=elemento
                flag=1
                
    return elem_maximo
    



def exportar_csv(mensaje):
    with open ("test.csv","w") as archivo:
        archivo.write(mensaje)


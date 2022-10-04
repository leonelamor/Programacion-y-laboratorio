from csv import list_dialects
import json
import re
def cargar_json(ruta:str):
    with open (ruta,"r")as archivo:
        data=json.load(archivo)
        lista_pokemones=data["pokemones"]
        lista_pokemones=list[dict](lista_pokemones)
    return lista_pokemones

lista_pokemones=cargar_json("Practica parcial(pokemones)\pokedex.json")

def mostrar(lista:list,key="evoluciones"):
    mensaje=""
    for elemento in lista:
        mensaje+=" Nombre: {0} \n Tipo: {1} \n {2}{3}\n ------------\n".format(elemento["nombre"],elemento["tipo"],key,elemento[key])

    return mensaje

def minimo(lista:list,key:str,orden):
    if (lista):
        minimo=0
    if (orden=="asc"):
        for i in range (len(lista)):
            if(lista[i][key]<lista[minimo][key]):
                minimo=i
        return minimo
    elif (orden=="desc"):
        for i in range (len(lista)):
            if(lista[i][key]>lista[minimo][key]):
                minimo=i
        return minimo
    else:
        return -1
            
def nahu_sort(lista,key,orden):
    lista_a_ordenar=lista.copy()
    lista_ordenada=[]
    while(len(lista_a_ordenar)>0):
        indice_minimo=minimo(lista_a_ordenar,key,orden)
        lista_ordenada.append(lista_a_ordenar.pop(indice_minimo))
    return  lista_ordenada





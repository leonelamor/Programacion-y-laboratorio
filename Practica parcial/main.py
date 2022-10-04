from cgitb import text
import json
import re 

def cargar_json(ruta:str)->list:
    '''
    Lo que hace esta funcion es cargar el archivo json para luego utilizarlo y a la vez formatearlo a un tipo lista de diccionarios
    Parametros recibidos : un string con la ruta de el archivo json
    retorna: una lista
    '''
    with open (ruta,"r") as archivo:
        data=json.load(archivo)
        lista_heroes=data["heroes"]
        lista_heroes=list[dict](lista_heroes)
    return lista_heroes

lista_personajes=cargar_json("Practica parcial\data_stark.json")

def func_mostrar(lista:list,key="altura")->str:
    '''
    Lo que hace esta funcion es formatear un mensaje para que muestre el nombre, la identidad y una key que nosotros le pasemos, en caso de no pasar va a tomar por default la key "altura"
    Parametros recibidos:lista y una key(opcional)
    Devuelve: un string con un mensaje formateado
    '''
    mensaje=""
    for elemento in lista:
        mensaje+="nombre: {0} - identidad: {1} {2}:{3}\n".format (elemento["nombre"], elemento["identidad"],key,elemento[key])
    return mensaje

'''def lista_h(lista_hero:list):
    lista_copia=lista_hero.copy()
    respuesta=input("Ingrese un N")
    lista_new=[]
    if(re.search("[0-9]",respuesta)):
        respuesta=int(respuesta)
        if(respuesta<=len(lista_copia)):
            for hero in lista_copia[:respuesta]:
                lista_new.append(hero)
            return lista_new'''

def buscar_minimo(lista:list,key:str,orden:str)->int:
    '''
    Lo que hace la funcion buscar minimo es buscar un minimo en una lista en la cual lo que tenemos que comparar son las claves.
    Parametros: lista una clave numerica a comparar y una orden de (asc) ascendente o (desc)descendente
    Devuelve un entero
    '''
    
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


def nahu_sort(lista:list,key:str,orden:str)->list:
    '''
    Esta funcion crea una nueva lista en la cual segun el orden que le demos nosotros con el tercer parametro va a ser ascendente o descendente ( reutiliza la funcion anterior para buscar un minimo)
    esta funcion se basa en claves numericas
    Parametros :lista , una clave , y el orden a ordenar (asc) o (desc)
    '''
    lista_a_ordenar=lista.copy()
    lista_ordenada=[]
    while(len(lista_a_ordenar)>0):
        indice_minimo=buscar_minimo(lista_a_ordenar,key,orden)
        lista_ordenada.append(lista_a_ordenar.pop(indice_minimo))
    return  lista_ordenada


def promedio(lista:list,key:str,menor_o_mayor:str)->list:
    '''
    Esta funcion devuelve una lista  la cual en base a una key nos va a mostrar los personajes que esten por debajo o por arriba de el promedio de esa key numerica.
    Parametros: lista  , una clave , y una eleccion en str que puede ser (mayores)(menores) 
    '''
    lista_copia=lista.copy()
    lista_impresa=[]
    contador=0
    acumulador=0
    for i in lista_copia:
        contador+=1
        acumulador+=i[key]
    promedio=acumulador/contador
    for elemento in lista_copia:
        if(menor_o_mayor=="mayores"):
            if(elemento[key]>promedio):
                lista_impresa.append(elemento)
        if(menor_o_mayor=="menores"):
            if(elemento[key]<promedio):
                lista_impresa.append(elemento)
    return lista_impresa


def heroes_por_inteligencia(lista:list,tipo_int:str)->list:
    '''
    Lo que hace es segun el parametro que nosotros le pasemos de tipo de inteligencia, retornar una lista en la cual se encuentre dicho valor
    parametros:lista y valor (good)(average)(high)
    devuelve=lista con el valor que le pasemos
    '''
    lista_copia=lista.copy()
    lista_impresa=[]
    for heroe in lista_copia:
        if(heroe["inteligencia"]==tipo_int):
            lista_impresa.append(heroe)
    return lista_impresa



def guardar_archivo(mensaje:str):
    with open ("Archivo.csv","w") as archivo:
        archivo.write(mensaje)



    
def buscar_heroe(lista,patron):
    lista_provisional=[]
    for elemento in lista:
        match=re.search(patron,elemento["identidad"],re.IGNORECASE)
        if(match):
            lista_provisional.append(elemento["nombre"])
    return lista_provisional

print(buscar_heroe(lista_personajes,"Tony stark"))



 
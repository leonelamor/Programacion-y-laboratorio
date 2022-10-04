from ast import Str
from imp import PY_CODERESOURCE
from data_pokemon import pokemones


'''
pokemones = [
        {
            "id": 1,
            "nombre": "bulbasaur",
            "tipo": ["planta"],
            "evoluciones": ["ivysaur", "venusaur"],
            "poder": 4,
            "fortaleza":["agua"],
            "debilidad":["fuego"]
        },
'''

def obtener_nombre_pokemon(pokemon:dict) ->str:
    '''
    Recibo un pokemon como parametro y retorna el valor de la key "nombre"
    Parametro: Diccionario de pokemon
    Retorno: Nombre como string
    '''
    return pokemon["nombre"]


def imprimir_pokemones(pokemones:list) ->None:
    '''
    Recibe la lista de pokemones y los imprime uno a uno
    Parametro: lista de pokemones
    Retorno:None
    '''
    if(len(pokemones))>0:
        for pokemon in pokemones:
            nombre_pokemones= obtener_nombre_pokemon(pokemon)
            print(nombre_pokemones)

def tiene_id_par(pokemon:dict)->bool:
    '''
    Recibe por parametro un diccionario y verifica que su id sea par, si es par retorna true o false
    Parametro: Diccionario 
    Retorno: booleano(true o false)
    '''
    if (pokemon["id"]%2==0):
        return True
    else:
        return False

def obtener_pokemon_id(pokemon:dict)->str:
    '''
    Recibe un parametro un diccionario y devuelve el id como string
    Parametro: Diccionario
    Retorno: String de el ID
    '''
    str_pokemon=str(pokemon["id"])
    return str_pokemon

def pokedex_imprimir_pokemones_id_par(pokemones:list)-> None:
    '''
    recibirá por parámetro
    la lista de pokemones y deberá imprimir solo los que cumplan con la condición de
    tener un ID par
    Parametro: Lista
    Retorno: none

    '''
    if (len(pokemones)>0):
        for pokemon in pokemones:
            if(tiene_id_par(pokemon)):
                nombre_pokemon=obtener_nombre_pokemon(pokemon)
                id_pokemon=obtener_pokemon_id(pokemon)
                print("El nobmre del pokemon: {0} El id del pokemon seria: {1}".format(nombre_pokemon,id_pokemon))


def id_multiplo_25(pokemones:dict)-> bool:
    '''
    Recibe por parametro un diccionario de pokemones y chequea si es multiplo de 25 devuelve un booleano (true o false)
    Parametro: Diccionario
    Retorno: booleano
    '''
    if(pokemones["id"]%25==0):
        return True
    else:
        return False

def pokedex_imprimir_pokemon_id_mul_25(pokemones:list) -> None:

    '''
    Recibe por parámetro una lista y checquea si es multiplo de 25, si es así printear aquellos pokemones que cumplen la condicion.
    Parametro: Lista
    Retorno: None
    '''
    if(len(pokemones)>0):
        for pokemon in pokemones:
            if(id_multiplo_25(pokemon)):
                nombre_pokemon_2 = obtener_nombre_pokemon(pokemon)
                print("El nombre del pokemon es : {0}".format(nombre_pokemon_2))





def nombre_format_pokemon(pokemon:dict)-> str:
    '''
    La funcion obtiene el numero y el id y lo formatea como string a > #0001 y nombre de pokemon
    parametro: Diccionario
    Retorno:String  con el id y el nombre del pokemon formateado

    '''

    nombre_pokemon=obtener_nombre_pokemon(pokemon)
    id_pokemon=obtener_pokemon_id(pokemon)
    nombre_y_id="El id es #00{0} - El nombre del pokemon es {1} " .format(id_pokemon,nombre_pokemon)
    nombre_y_id=str(nombre_y_id)
    return nombre_y_id


def pokedex_imprimir_nombres_poke_fmt(pokemones:list)->None:
    '''
    La funcion obtiene el numero y el id y lo formatea a > #0001 y nombre de pokemon
    parametro: lista
    retorno:None
    '''
    if(len(pokemones)>0):
        for pokemon in pokemones:
            id_y_nombre=nombre_format_pokemon(pokemon)
            print(id_y_nombre)


def calcular_max_dato(pokemones:list,maximo:str,clave:str)->Str:
    '''
    Esto calcula el dato maximo( ya sea poder o id)
    parametro: una lista, un string(con el maximo) y otro string(con la clave)
    Retorno: Un string con el nombre

    '''
    maximo=pokemones[0][clave]
    for pokemon in pokemones:
        if(pokemon[clave]>maximo):
            maximo=pokemon[clave]
    return maximo

#print(calcular_max_dato(pokemones,"5","poder"))


def obtener_lista_pokemones(pokemones:list,clave:str,valor:int)->None:
    '''
    Esto obtiene una lista de pokemones
    Los parametros son: Una lista, un string, un entero
    Retorno:None
    '''
    for pokemon in pokemones:
        if (pokemon[clave]==valor):
            lista_nombre=pokemon["nombre"]
            print(lista_nombre)

def string_max_dato(pokemones:list,max:str,clave:str):
    pokemon_max=(calcular_max_dato(pokemones,max,clave))
    obtener_lista_pokemones(pokemones,clave,pokemon_max) 


string_max_dato(pokemones,"20","poder")

 






















from data_stark import lista_personajes



def obtener_nombre(heroes:dict):
    nombre=heroes["nombre"]
    nombre_formateado="Nombre:{0}".format(nombre)
    return nombre_formateado


def imprimir_dato(heroes:str):
    print(heroes)

def stark_imprimir_nombres_heroes(heroes:list):
    if len(heroes)>0:
        for heroe in heroes:
            nombre=obtener_nombre(heroe)
            imprimir_dato(nombre)
    else:
        return 1

def obtener_nombre_y_dato(heroes:dict,clave:str):
    nombre=obtener_nombre(heroes)
    key=heroes[clave]
    nombre_formateado="{0} | altura:{1}".format(nombre,key)
    return nombre_formateado

print(obtener_nombre_y_dato(lista_personajes[0],"altura"))


def stark_imprimir_nombres_alturas(heroes:list):
    if len(heroes)>0:
        for heroe in heroes:
            print(obtener_nombre_y_dato(heroe,"altura"))
    else:
        return 1



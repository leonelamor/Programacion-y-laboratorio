
from asyncio.windows_events import NULL

from data_stark import lista_personajes
'''
  {
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
  },
'''
def extraer_iniciales(nombre_heroe:str):


    if(len(nombre_heroe)>0):
        nombre_heroe=nombre_heroe.upper()
        nombre_heroe=nombre_heroe.replace("THE ","")

        nombre_heroe=nombre_heroe.replace("-"," ")
        
        nombre_parte=nombre_heroe.split(" ")
        mensaje=""
        for name in nombre_parte:
            mensaje+=name[0]+"."
        return mensaje
    else:
        return "N/A"
    


def definir_iniciales_nombre(heroe:dict):
    retorno=False
    if(type(heroe)==type(dict()) and "nombre" in heroe.keys()):
         heroe["iniciales"]=extraer_iniciales(heroe["nombre"])
    retorno=True

    return retorno


def agregar_iniciales_nombre(lista_heroes:list[dict])->bool:
    
    retorno=True 
    if (type(lista_heroes)== type(list()) and len(lista_heroes)>0):
        for heroe in lista_heroes:
            if(not definir_iniciales_nombre(heroe)):
                retorno=False
                break


    if(not retorno):
        print("Error")

    return retorno


def stark_imprimir_nombres_con_iniciales(lista_heroes):
    for heroes in lista_heroes:
        agregar_iniciales_nombre(lista_heroes)
        nombre_formateado="*{0} ({1})".format(heroes["nombre"],heroes["iniciales"])
        print(nombre_formateado)



def generar_codigo_heroe(id_heroe:int,genero_heroe:str)->str:
    if(type(id_heroe)==type(int()) and (genero_heroe=="M" or genero_heroe=="F" or genero_heroe=="NB")):
        if(genero_heroe!="" and genero_heroe !=NULL):
            if(genero_heroe=="NB"):
                id=str(id_heroe).zfill(7)
            else:
                id=str(id_heroe).zfill(8)
            id_genero_formateado="{0}-{1}".format(genero_heroe,id)
            return id_genero_formateado
    else:
        return "N/A"



def agregar_codigo_heroe(heroe:dict,id_heroe):
    retorno=True
    if(len(heroe)>0):
        heroe["codigo_heroe"]=generar_codigo_heroe(id_heroe,heroe["genero"])
        if(len(heroe["codigo_heroe"])!=10):
            retorno=False    
    return retorno


def stark_generar_codigos_heroes(lista_heroes:list):

    if(len(lista_heroes)>0):

        contador=0
        for heroe in lista_heroes:
            if(type(heroe)==type(dict())):
                if("genero" in heroe.keys()):
                    agregar_codigo_heroe(heroe,contador)
                    contador+=1
                    heroe_codigo=heroe["codigo_heroe"]
                    print(heroe_codigo)
                else:
                    return print("El origen de datos no contiene el formato correcto")
                    
def sanitizar_entero (numero_str:str):
    retorno=-3
    if(numero_str.find("-")>=0):
        if((numero_str.replace("-","")).isdecimal()):
            retorno= -2

    elif(numero_str.isnumeric()==False):
        retorno= -1
    else:
        retorno= int(numero_str)
    
    return retorno


 
    
print(sanitizar_entero("a-3"))





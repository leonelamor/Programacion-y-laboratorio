from itertools import product
from math import prod


lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio":300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}



# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'

def prueba1():

    '''
    msg_error="Key inexistente"
    producto=input("Ingrese un producto \n >")
    prod_dict=lista_precios.get(producto,"El articulo no se encuentra en la lista")
    if not type (prod_dict)==str:
        precio=prod_dict.get("precio","Key inexistente")
        if(precio==msg_error):
            print("ERROR NO EXISTE LA KEY")
        else: 
            print("El precio de {0} es {1}")
    else:
        print(prod_dict)
    '''


def prueba2():
    '''
    cantidad=input("Ingrese la cantidad \n >")
    cantidad=int(cantidad)
    if(producto in lista_precios.keys()):
        precio=lista_precios[producto]["precio"]
        stock=lista_precios[producto]["stock"]
        precio_total=precio*cantidad
        print("El precio unitario es de: {0} El stock es de : {1}".format(precio,stock))
        print("Precio total es de: {0}".format(precio_total))
    else:
        print("el articulo no se encuentra en la lista")
    '''


def ejercicio_uno_dos():
    msg_error="key inexistente"
    producto=input("Ingrese un producto \n >")
    prod_dict=lista_precios.get(producto,"El articulo no se encuentra en la lista")
    if(producto in lista_precios.keys()):
            precio=prod_dict.get("precio","key inexistente")
            if (precio!=msg_error):
                    cantidad=input("Ingrese una cantidad \n >")
                    cantidad=int(cantidad)
                    precio_final=precio*cantidad
                    stock= prod_dict.get("stock","key inexistente")
                    print("El precio es: {0} El stock es {1}".format(precio,stock))
                    print("El precio final es{0}".format(precio_final))
            else:
                print("ERROR NO EXISTE LA KEY PRECIO")

    else:
        print(prod_dict)
        
def ejercicio_tres():
    nueva_fruta=input("Ingrese una nueva fruta >")
    precio=int(input("Ingrese el precio>"))
    unidad_medida_nuevo=input("Ingrese la unidad de medida >")
    stock_nuevo=input("Ingrese stock >")
    lista_precios.update({nueva_fruta:{"precio":precio}})
    lista_precios[nueva_fruta].update({"unidad_medida":unidad_medida_nuevo})
    lista_precios[nueva_fruta].update({"stock":stock_nuevo})
    print(lista_precios)

def ejercicio_cuatro():
    for fruta in lista_precios:
        print(fruta)

def ejercicio_cinco():
    nombre_a_eliminar=input("Ingrese un nombre de fruta que quiera eliminar >")

    if(nombre_a_eliminar in lista_precios):
        lista_precios.pop(nombre_a_eliminar)
        print(lista_precios)
    else:
        print("el mensaje 'el articulo no se encuentra en la lista")

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)


# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios


# Punto 4: imprimir el listado de frutas (solo su nombre)


# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

 


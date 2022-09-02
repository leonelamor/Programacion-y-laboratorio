'''
lista=[1,2]
lista.append(3)
print(lista)
lista[1]=5

lista_temas=["T1","T2","T3","T4"]
for tema in lista_temas: #esto simplifica mucho la lectura ... el agregarle un " tema " y no un i 
    print(tema)

dic={}# diccionario vacio
dic= {"clave":"valor"}
for key in dic:
    print(key)

dic ["Nombre"]="juan"
print (dic)

'''
'''cant_empleados=3
lista_nombres=[]
lista_apellidos=[]
for i in range (cant_empleados):
    nombre=input("N")
    apellidos=input("A")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellidos)


#for i in range(len(lista_nombres)):

#otra solucion
for i in range (cant_empleados):
    print("{0} - {1} - {2}".format(i, lista_nombres[i] , lista_apellidos[i])) 

'''

cant_empleados=3
lista_empleados=[]

for i in range (cant_empleados):
    nombre=input("N")
    apellidos=input("A")
    dic_empleado={}
    dic_empleado["Nombre"]=nombre
    dic_empleado["Apellido"]=apellidos
    lista_empleados.append(dic_empleado)
    
for empleado in lista_empleados:
    print(empleado["Nombre"]) #aca accedemos al indice nombre dentro de la lista 



#otra solucion






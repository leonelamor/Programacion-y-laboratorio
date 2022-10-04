import main
def app():
    while(True):
        print('''
        1-Listar los últimos N pokemones. El valor de N será ingresado por el usuario
        2-Ordenar y Listar pokemones por poder. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)
        3-Ordenar y Listar pokemones por ID. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc) 
        4-Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo) 
        y mostrar si quiere menores(menor) o mayores(mayor) en comparacion
        5-Buscar pokemones por tipo
        6- Exportar a CSV la lista de pokemones
        7- Salir
        
        ''' )






        respuesta=input(">")
        if(respuesta=="1"):
            tope=input("Hasta que numero desea imprimir?")
            tope=int(tope)
            print(main.mostrar(main.lista_pokemones[:tope]))
        elif(respuesta=="2"):
            input_usuario=input("Quiere ordenar los pokemones de forma descendente o ascendente")
            if(input_usuario=="asc"):
                print(main.mostrar(main.nahu_sort(main.lista_pokemones,"poder","asc"),"poder"))
            elif(input_usuario=="desc"):
                print(main.mostrar(main.nahu_sort(main.lista_pokemones,"poder","desc"),"poder"))


        elif(respuesta=="3"):
            pass
        elif(respuesta=="4"):
            pass
        elif(respuesta=="5"):
            pass
        elif(respuesta=="6"):
            pass
        elif(respuesta=="7"):
            pass
    
app()
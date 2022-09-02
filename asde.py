
 '''           heroe_reclutado_prov=heroes_info[heroes] #Accedo a la info por la clave 
            heroe_reclutado_prov["nombre de heroe"]=heroe#creo una clave llamada nombre de heroe y le doy el valor de heroe
            heroe_reclutado_prov["Habilidades"]=set(heroe_reclutado_prov["Habilidades"])#Seteo el valor de la clave habilidades 
            heroe_reclutado_prov["Origen"]= [heroe_reclutado_prov["Origen"]]# De prueba ... armo una lista con la clave origen
            heroe_reclutado_prov["Prueba"]="Hi"# De prueba ... hago una clave llamada prueba con valor hi
            
            heroes_reclutados.append(heroe_reclutado_prov)

for asd in heroes_reclutados:
    print(asd)
'''

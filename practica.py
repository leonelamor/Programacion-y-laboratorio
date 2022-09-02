heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]
heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}
heroes_reclutados=[]
for heroe in heroes_para_reclutar:
    for heroes in heroes_info:
        if(heroes==heroe):
            dic_nuevo={"Shazam":{"ID":heroes_info["Shazam"]["ID"], "habilidades":set(heroes_info["Shazam"]["Habilidades"]), "origen":heroes_info["Shazam"]["Origen"],"Identidad":heroes_info["Shazam"]["Identidad"] }}
            dic_nuevo["Power Girl"]={}
            dic_nuevo["Power Girl"]["ID"]=heroes_info["Power Girl"]["ID"]
            dic_nuevo["Power Girl"]["Origen"]=heroes_info["Power Girl"]["Origen"]
            dic_nuevo["Power Girl"]["Habilidades"]=set(heroes_info["Power Girl"]["Habilidades"])
            dic_nuevo["Power Girl"]["Identidad"]=heroes_info["Power Girl"]["Identidad"]
            dic_nuevo["Wonder Woman"]={}
            dic_nuevo["Wonder Woman"]["ID"]=heroes_info["Wonder Woman"]["ID"]
            dic_nuevo["Wonder Woman"]["Origen"]=heroes_info["Wonder Woman"]["Origen"]
            dic_nuevo["Wonder Woman"]["Habilidades"]=set(heroes_info["Wonder Woman"]["Habilidades"])
            dic_nuevo["Wonder Woman"]["Identidad"]=heroes_info["Wonder Woman"]["ID"]
            dic_nuevo["Super Girl"]={}
            dic_nuevo["Super Girl"]["ID"]=heroes_info["Super Girl"]["ID"]
            dic_nuevo["Super Girl"]["Origen"]=heroes_info["Super Girl"]["Origen"]
            dic_nuevo["Super Girl"]["Habilidades"]=set(heroes_info["Super Girl"]["Habilidades"])
            dic_nuevo["Super Girl"]["Identidad"]=heroes_info["Super Girl"]["Identidad"]



print(dic_nuevo)
            










    
    
    

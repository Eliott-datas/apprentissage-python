import json

chemin = r"C:\Users\Utilisateur\Documents\Apprentissage_python\apprentissage-python\fichier.json"

with open(chemin, "r") as f:
    datas = json.load(f)
    
datas.append("HEHE")

with open(chemin, "w") as f:
    json.dump(datas,f, indent=4)
    
    
    
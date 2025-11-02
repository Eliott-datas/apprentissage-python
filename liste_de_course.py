import json
from pathlib import Path
import sys

CUR_FILE = Path(__file__).resolve()
CUR_DIR = CUR_FILE.parent
LISTE_PATH = CUR_DIR / "liste.json"

if LISTE_PATH.exists():
    with open(LISTE_PATH, "r") as f:
        liste = json.load(f)

else :
    liste = []

MENU_CHOICES = ["1","2","3","4","5"]

MENU = """Choisissez parmi les 5 options suivantes
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
Votr choix : """


while True :
    
    choix = ""
    
    while choix not in MENU_CHOICES:
        choix = input(MENU)
        
    if choix == "1":       
        element = ""
        while not element:               
            element = input("Entrez le nom d'un élément à ajouter à la liste de course : ")
            if not element:
                print("Vous n'avez rien rentré")
        liste.append(element)  
  
    if choix == "2":     
        if not liste:
            print("la liste est vide")  
        else :
            element_a_supprimer = input("Quel élement supprimer : ")
            if element_a_supprimer in liste:
                liste.remove(element_a_supprimer)
                print(f" {element_a_supprimer} à bien été supprimer de la liste de course")
            else :
                print(f"{element_a_supprimer} n'est pas dans la liste de course")   
           
    elif choix =="3":
        if liste:
            print("Voici votre liste de course :")  
            for i in range(len(liste)):
                print(f"{i+1}. {liste[i]}")
        else:
            print("la liste de course est vide")
    
    elif choix =="4":
        if liste:  
            liste.clear()
        else:
            print("la liste de course est deja vide")
    
    elif choix == "5":
        print("Aurevoir")
        with open(LISTE_PATH, "w") as f:    
            json.dump(liste, f, indent=4)
        sys.exit()
    
    print("-" * 50)
    


    
 
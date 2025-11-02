
choix_possible = ["1","2","3","4","5"]
choix = ""
liste_de_course = []

while True :
    
    while choix not in choix_possible:
        choix = input(
            "-----------------------------------------\n"
            "Choisissez parmi les 5 options suivantes\n"
            "1: Ajouter un élément à la liste\n"
            "2: Retirer un élément de la liste\n"
            "3: Afficher la liste\n"
            "4: Vider la liste\n"
            "5: Quitter\n"
            "--> Votre choix : "
        )
        
    if choix == "1":       
        element = ""
        while not element:               
            element = input("Entrez le nom d'un élément à ajouter à la liste de course : ")
            if not element:
                print("Vous n'avez rien rentré")
        liste_de_course.append(element) 
        choix = "" 
        
    if choix == "2":     
        if not liste_de_course:
            print("la liste est vide")  
        else :
            element_a_supprimer = input("Quel élement supprimer : ")
            if element_a_supprimer in liste_de_course:
                liste_de_course.remove(element_a_supprimer)
                print(f" {element_a_supprimer} à bien été supprimer de la liste de course")
            else :
                print(f"{element_a_supprimer} n'est pas dans la liste de course")
        choix = ""    
           
    elif choix =="3":
        if liste_de_course:
            print("Voici votre liste de course :")  
            for i in range(len(liste_de_course)):
                print(f"{i}. {liste_de_course[i]}")
        else:
            print("la liste de course est vide")
        choix = "" 
    
    elif choix =="4":
        if liste_de_course:  
            liste_de_course.clear()
        else:
            print("la liste de course est deja vide")
        choix = "" 
    
    elif choix == "5":
        print("Aurevoir")
        break
    


    
 
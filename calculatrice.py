a = b = ""

while not(a.isdigit() and b.isdigit()):
    
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    if not(a.isdigit() and b.isdigit()):
        print("entrez des nombres valides : ")
    
somme = int(a) + int(b)
print(f"le resultats de {a} + {b} est égale à {somme}")
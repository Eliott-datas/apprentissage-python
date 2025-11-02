import os
chemin = r'C:\Users\Utilisateur\Documents\Apprentissage_python\apprentissage-python'

dossier = os.path.join(chemin, 'dossier', 'sous dossier')

if not os.path.exists(dossier):
    os.makedirs(dossier)

else :
    os.removedirs(dossier)



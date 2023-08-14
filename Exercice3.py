with open('fichier .txt', 'r') as file:
    contenu = file.read()

contenu_modifie = contenu.replace('\n', ' ')

print(contenu_modifie)
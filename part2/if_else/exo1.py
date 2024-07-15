# Fonction pour trier une liste
def trier_liste(liste, ordre):
    if ordre == "c":                   # "croissant"
        return sorted(liste)
    elif ordre == "d":                # décroissant
        return sorted(liste, reverse=True)
    else:
        return "Ordre non reconnu. Utilisez 'croissant' ou 'décroissant'."

# Liste de nombres
nombres = [34, 12, 45, 67, 23, 89, 1, 7, 56]

# Choix de l'utilisateur
ordre = input("Voulez-vous trier la liste en ordre croissant ou décroissant ? ")

# Trier et afficher la liste
resultat = trier_liste(nombres, ordre)
print("Liste triée :", resultat)

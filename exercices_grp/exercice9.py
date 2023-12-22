# Je crée mes 4 fonctions



#déclarer dictionnaire:
data_base = {}

# 1ère fonction: obtenir le tuple à partir du prénom de l'individu
def consult_data_base(data_base, nom):
    if nom in data_base:
        return data_base[nom]
    else:
        print(f"Le nom {nom} n'est pas présent dans la base de données.")
        return None

# Création fonction remplissage du dictionnaire
def filling_dict(data_base):
    nom = input("Entrez le nom de l'individu : ")
    age = int(input("Entrez l'âge (en années) : "))
    sexe = input("Entrez le sexe (M/F) : ")
    taille = float(input("Entrez la taille (en mètres) : "))




    # Vérifiez si le nom n'est pas déjà présent 
    if nom not in data_base:
        data_base[nom] = (age, sexe, taille)
        print(f"{nom} a été ajouté à la base de données.")
    else:
        print(f"{nom} est déjà présent dans la base de données.")

# Fonction pour sauvegarder dict dans fichier txt nommé data.txt
def save_my_dict(data_base, nom_fichier):
    with open(nom_fichier, "a") as file: #commandes afin d'importer code dans un fichier txt "a" >> ajout
        for nom, info in data_base.items():
            ligne = f"{nom},{info[0]},{info[1]},{info[2]}\n" 
            file.write(ligne) 


# Fonction pour reconstituer le dictionnaire via fichier txt
def load_dict_from_file(nom_fichier):
    data_base = {}
    
    with open(nom_fichier, "r") as file: #r pour read >> je lis le doc txt pour en importer les infos sur mon code
            for ligne in file:
                nom, age, sexe, taille = ligne.strip().split(',')
                data_base[nom] = (int(age), sexe, float(taille))
    
    return data_base

# Demander à l'utilisateur ce qu'il souhaite faire
choix = input("Que souhaitez-vous faire? compléter ou consulter : ")

if choix == "compléter":
    filling_dict(data_base) #j'appelle mes fonctions relatives à la complétion
    save_my_dict(data_base, "data.txt")
elif choix == "consulter": #j'appelle mes fonctions relatives à la consultation
    nom_recherche = input("Nom à consulter : ")
    result = consult_data_base(data_base, nom_recherche)
    if result:
        print(f"Nom : {nom_recherche} - âge : {result[0]} ans - sexe : {result[1]} - taille : {result[2]} m")
else:
    print("Choix non valide.")

# les impairs
# Important : je cherche a faire des fonctions que je vais lancer ensuite
# declarer tes 2 nombres? dans la fonction (a priori)
# =>recuperer l input des nombres x et y à fournir par l utilisateur

# declarer ta fonction
def trouverImpairs():
    #declarer les entrées x et y de l utilisateur et les récupérer via un controle(je veux des decimaux)
    x=""
    y=""
    
    #je place les entrées de l utilisateur sous conditions : si x.isdecimal() est 
    while not x.isdecimal():
        x = input('indiquer le 1 er nombre: ')
        break
    
    while not y.isdecimal():
        y = input('indiquer le second nombre: ')
        break   
    print(x,y)
#je recupere x et y mais je dois faire un try except pour gerer la situation en cas d erreur(le nom de l erreur est fourni par le terminal)
    try:
# determiner les parties entieres X et Y(== entiers referents) des strings(from input) x et y  via un cast: eval() via math(passage str à float) puis int(float à int)
        X = int(eval(x))
        Y = int(eval(y))
        maListe = list()
# ordonner entre X ET Y :si X > Y alors X = int(y) et Y = int(x)
        if X > Y:
            X = int(eval(y))
            Y = int(eval(x))
# determiner la liste des entiers entre ces deux entiers referents == maListe(la remplir via un parcours entre X et Y)
        for i in range (X,Y+1):
        #si i % 2 != 0 alors  i impair, je l'ajoute a la liste que je remplis d impairs
            if((i % 2) != 0):
                maListe.append(i)
# retourner le resultat
        print('liste des impairs entre ',x, 'et ',y,':\n',maListe)
    except (NameError, SyntaxError):
        print("entrée incorrecte, refaites votre choix")
        trouverImpairs()

trouverImpairs()
    

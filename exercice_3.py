import random

def plus_grands_num(a, b):

    list_dimension = (a, b)
    #creation de l'algo qui génère une liste de 100 entiers 
    list_dimension = random.choices(range(a, b+1), k=100)
    #'+1' permet d'intégrer le dernier chiffre
    return list_dimension


result = plus_grands_num(0, 99)
print(result)




# def plus_grands_num(a, b):

#     list_dimension = (a, b)
#     #creation de l'algo qui génère une liste de 100 entiers 
#     list_dimension = random.choices(range(a, b+1), k=100)
#     #'+1' permet d'intégrer le dernier chiffre
#     return list_dimension


# result = plus_grands_num(0, 99)
# print(result)
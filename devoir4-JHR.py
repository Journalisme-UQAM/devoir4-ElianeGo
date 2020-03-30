# coding : utf-8

### BONJOUR ÉLIANE
### J'APPRÉCIE QUE TU LAISSES TOUTES TES TENTATIVES ET DIFFÉRENTS COMMENTAIRE DANS TON SCRIPT!

import csv, spacy
#module pour compter les éléments
from collections import Counter

tal = spacy.load("fr_core_news_md")

#pour que spacy considère certains mots comme vides :
tal.Defaults.stop_words.add("y")
tal.Defaults.stop_words.add("C'")
tal.Defaults.stop_words.add("d'")
tal.Defaults.stop_words.add("c'")
#pour ramener des mots vide donc les retrancher de la liste:
tal.Defaults.stop_words.remove("gens")

# rmartino = "martino.csv"
rmartino = "../martino.csv" ### ICI, JE CHANGE SIMPLEMENT LE "CHEMIN" VERS LE FICHIER POUR L'AJUSTER À CE QUE J'AI DANS MON ORDI

# PremierMot = "islam"
# islam = "PremierMot"
# musulm = "DeuxiemeMot"
# DeuxiemeMot = "musulm"

f = open(rmartino)
interventions = csv.reader(f)

#créer une variable qui va compter les mots
# tousMots = []
#créer une variable qui va compter les paires de mots
bigrams = []
bigram = []

freq = Counter(bigrams)

for inter in interventions:
    # print(inter[3])
    doc = tal(inter[3])
    print(inter[1]) ### J'IMPRIME LA DATE DE LA CHRONIQUE, HISTOIRE DE VOIR TON SCRIPT PROGRESSER
    
    # for token in doc: ### CETTE BOUCLE N'EST PAS UTILE; TU FAIS QUELQUE CHOSE DE SEMBLABLE À LA LIGNE 47
    ### LIGNE 47 QUI N'AVAIT PAS BESOIN DE SE TROUVER DANS LADITE BOUCLE, DONC JE L'AI INDENTÉE D'UN CRAN VERS LA GAUCHE
    ### C'EST CELA QUI RALENTISSAIT SURTOUT TON SCRIPT; IL ROULE BCP PLUS VITE MAINTENANT!
    lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    #    print(lemmes)
    # comment enlever les mots vides
    #    for lemme in lemmes : 
    #        if PremierMot = islam.add
    #        print(lemme)
    #        elif DeuxiemeMot = musulm.add
    #        print(lemme)

    for x, y in enumerate(lemmes[:-1]):
            ### ICI, TU AS INDENTÉ TON CODE D'UN CRAN DE TROP VERS LA DROITE
            # bigrams = "{} {}".format(lemmes[x], lemmes[x+1])

        ### JE RAMÈNE TOUT D'UN CRAN VERS LA GAUCHE
        bigrams = "{} {}".format(lemmes[x], lemmes[x+1])
        if "islam" in bigrams or "musulm" in bigrams: ### EXCELLENTE SOLUTION DE RECHANGE, PLUS SIMPLE QUE CELLE QUE JE PROPOSE DANS LE CORRIGÉ! :)
            print(bigrams)
            #à chaque fois je ne comprenais pas pourquoi ça imprimait tous les bigrams, je finissais pas l'arreter car c'était trop long, mais j'ai compris que c'était juste à cause que je faisais print tous les bigrams!
            ### AH, POURTANT, J'AI "DÉCOMMENTÉ" TON "PRINT(BIGRAMS)" ET ÇA N'IMPRIME QUE LES PAIRES DE MOTS DANS LESQUELLES ON TROUVE LES EXPRESSIONS RECHERCHÉES
            bigram.append(bigrams)
           
        # print(freq.most_common(50))

            # bigrams.append(bigrams)
    # ca imprime une liste vide, je continue les essais... 
    # j'ai essayé autre chose et je pense que ca m'a imprimé toutes les paires de mots ... 
    ### je veux mettre la condition d'imprimer les paires avec les mots recherchés seulement 
    ### au bout de plusieurs essais je suis fâchée, en 10 minutes de roulement il n'y a finalement rien qui a imprimé?? en plus d'entendre fort la fan de mon ordi, je n'aime pas lui faire vivre ça et que ça donne rien... 
    ### OUI, SPACY PEUT ÊTRE TAXANT SUR LE PROCESSEUR D'UN ORDI OU SUR SON PROCESSEUR GRAPHIQUE.
    # if islam == "PremierMot" :
    #     bigrams.append("islam")
    # elif musulm == "DeuxiemeMot" : 
    #     bigrams.append("musulm")
        
    # if islam == "PremierMot" :
    #     bigrams.append("islam")
    # elif musulm == "DeuxiemeMot" : 
    #     bigrams.append("musulm")
freq = Counter(bigram)
# most_occur = Counter.most_common(50) ###le most_occur est une technique trouvée sur internet que j'ai voulu tester
# print(most_occur) 
print(freq.most_common(50))
### on dirait que je n'ai fait qu'un essaie, mais ca fait plusieurs fois que je change mes indentation ou mes if et elif... a chaque fois avec un long délai pour que le print se fasse

### IL EST VRAI QUE TON SCRIPT ROULAIT PLUS LENTEMENT; J'ESPÈRE QUE LES COMMENTAIRES ET LES CHANGEMENTS QUE J'AI EFFECTUÉS T'AIDENT À COMPRENDRE POURQUOI?
# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt 
from math import log, exp 
from random import sample, random 
%matplotlib inline

def fichier2str(nom_fichier):
    """ Renvoie le contenu du fichier sous forme de chaîne de caractères. """ 
    with open(nom_fichier, 'r') as f: 
        chaine = f.read() 
    return chaine 

def ind(car): 
    """ Renvoie l'indice du caractère dans l'alphabet. """ 
    if car != ' ': 
        return ord(car)-97 
    else: 
        return 26 

def alphabet(): 
    A = [] 
    for code in range(97, 123): 
        A.append(chr(code)) 
    A.append(chr(32)) 
    return A 

def freq_bigrammes(chaine,alphabet):
    """ Renvoie le tableau 2D des fréquences d'apparition des lettres et des bigrammes (suite de deux lettres consécutives). """

    n = len(alphabet) 
    m = len(chaine)
    
    # tableau des fréquences des bigrammes 
    freq_bigr = np.zeros((n, n))
    
    # tableau des fréquences 
    freq = np.zeros((n,)) 
    for i in range(m-1): 
        freq[ind(chaine[i])] += 1 
        freq_bigr[ind(chaine[i]), ind(chaine[i+1])] += 1
    
    # cas de la dernière lettre 
    freq[ind(chaine[m-1])] += 1
    return freq/m, freq_bigr/m 

def affiche_freq_lettres(freq, A): 
    """ Affiche l'histogramme des fréquences des lettres en français à partir d'un texte de référence. """ 
    fig = plt.figure() 
    fig, ax = plt.subplots() 
    X = [i for i in range(27)] 
    ax.bar(X, freq) 
    ax.set_title("Fréquences d'apparition des lettres") 
    ax.set_xlabel("Lettres") 
    ax.set_xticks(X) 
    ax.set_xticklabels(A) 
    ax.set_ylabel("Frequence") 

def affiche_freq_bigr(freq_bigr, A): 
    fig, ax = plt.subplots(figsize=(10, 10)) 
    ax.pcolormesh(freq_bigr, cmap='summer') 
    ax.axis('equal') 
    X = [i+0.5 for i in range(27)] 
    ax.set_xticks(X) 
    ax.set_xticklabels(A) 
    ax.set_yticks(X) 
    ax.set_yticklabels(A) 
    for i in range(27): 
        for j in range(27): 
            ax.text(i+0.1, j+0.4, A[i] + A[j]) 
            
def calcul_P(chaine,alphabet): 
    """ Renvoie la matrice des proba Pxy (proba d'avoir l'enchaînement des deux caractères x et y). """ 
    n = len(aphabet)
    freq, big = freq_bigrammes(chaine,alphabet) 
    P = np.zeros((n, n))
    for x in range(n): 
        for y in range(n): 
            if freq[x] != 0: 
                P[x, y] = big[x, y]/freq[x] 
            else:
                P[x, y] = 0
    return P

def L(chaine, P): 
    """ Renvoie la vraisemblance d'une chaîne. Pour chaque caractère car du texte, on trouve son indice dans l'alphabet, ainsi que l'indice du caractère suivant. On en déduit la proba P correspondant à cet enchaînement. P est la matrice des probas calculée sur un texte de référence. """ 
    S = 0 
    for i in range(len(chaine)-1): 
        pxy = P[ind(chaine[i]), ind(chaine[i+1])] 
        if pxy < 1e-9: 
            S -= 9 
        else: 
            S += log(pxy)
    return S

def remplacement(chaine, alphabet): 
    """ Réalise une permutation circulaire sur la chaine pour trois lettres de l'alphabet tirées au hasard. """ 
    li_chaine = list(chaine)
    # On choisit trois lettres au hasard dans l'alphabet 
    li_sample = sample(alphabet, 3)
    for i in range(len(li_chaine)): 
        j = 0 
        go = True 
        while j < 3 and go == True: 
            if li_chaine[i] == li_sample[j]: 
                li_chaine[i] = li_sample[(j+1)%3] 
                go = False 
                j += 1
    chaine_retour = ''.join([car for car in li_chaine])
    return chaine_retour    

def dechiffrement(texte, n, P, alphabet): 
    """ Déchiffre le message par une méthode de recuit simulé. n est le nombre d'itérations de l'algorithme.
    P est la matrice des fréquences des bigrammes. alphabet est une liste des caractères autorisés. """
    liste_L = [] 
    i_opt = 0
    for i in range(1, n): 
        # on permute 3 caractères au hasard 
        nouveau_texte = remplacement(texte, alphabet) 
        L1 = L(nouveau_texte, P) 
        L0 = L(texte, P)

        # si le nouveau texte est plus vraisemblable que le précédent on le garde
        if L1 > L0: 
            texte = nouveau_texte 
            liste_L.append(L1) 
            meilleur_texte, L_opt = texte, L1
       
        # sinon on le garde avec une certaine proba qui décroît au cours du temps
        else: 
            B = log(i)/10 
            p = exp( B * (L1 - L0)) 
            if p >= random(): 
                texte = nouveau_texte 
                liste_L.append(L1)
     
    return meilleur_texte, L_opt, liste_L


chaine = fichier2str('texte_reference.txt')
A = alphabet()
freq, freq_bigr = freq_bigrammes(chaine, A) 
affiche_freq_lettres(freq, A)
affiche_freq_bigr(freq_bigr, A)
P = calcul_P(chaine, A) 
texte_chiffre = fichier2str('texte_a_dechiffrer.txt') 
n_iter = 10000
texte, L_opt, liste_L = dechiffrement(texte_chiffre, n_iter, P, A) 
print(texte)

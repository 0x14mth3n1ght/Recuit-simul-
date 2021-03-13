# Recuit-simul-

Le but est de déchiffrer un texte en s'appuyant sur la probabilité d'apparition des lettres de l'alphabet dans un texte. 
Ici, notre alphabet sera composé des lettres minuscules de l'alphabet français ('a', 'b',..., 'z') et du caractère espace (' '). 
Les fréquences des lettres et des bigrammes (deux lettres qui se suivent) seront déterminées à partir d'un texte de référence contenu dans le fichier texte texte_reference.txt.
Le texte à déchiffrer est stocké dans le fichier texte texte_chiffre.txt. Le principe du dechiffrement
consiste à permuter toutes les lettres de l'alphabet entre elles (par exemple, tous les 'a' deviennent des 't', tous les 'u' deviennent des 'o', etc). On ne connaît pas quelle permutation a été choisie. 


Pour un texte donné, si x et y sont deux caractères, on définit la quantité Px;y comme la proportion de y parmi les caractères qui suivent x : 

![equation](http://www.sciweavers.org/upload/Tex2Img_1615581681/render.png)

Où fx correspond à la fréquence d'apparition de la lettre x, et fxy à la fréquence d'apparition du
bigramme xy. Par exemple, Pet doit être grand, tandis que Pjw doit être faible. 
On appellera vraisemblance d'un texte t relative à la matrice P la quantité : 

![equation](http://www.sciweavers.org/download/Tex2Img_1615582284.jpg)

Où ti représente le ième caractère du texte t. 


Le procédé de recuit est utilisé en métallurgie pour obtenir une configuration des atomes du cristal métallique correspondant à un miminum de son énergie E. 
Il consiste à alterner des phases de refroidissement et de recuit (réchauffage du matériau) pour atteindre le minimum global de la fonction E, et non pas seulement le minimum local qui aurait été atteint par un refroidissement non contrôlé. 
Par analogie, l'algorithme du recuit simulé est une méthode utilisée dans les problèmes d'optimisation pour tenter de trouver l'extremum global d'une fonction E (contrairement aux algorithmes
gloutons qui atteignent par définition un extremum local). Le principe est de choisir à chaque itération la variation de l'ensemble des variables du modèle qui optimise la valeur de la fonction, mais tout en continuant d'explorer l'espace des variables pour se laisser une chance de s'extraire
d'un extremum local . Au début le paramètre T (analogie avec la température) est élevé et on explore beaucoup l'espace
des variables (la probabilité de ne pas rejeter une solution qui n'optimise pas E est forte).

Au cours de l'algorithme on fait décroître le paramètre T , on explore de moins en moins et l'algorithme
devient glouton pour atteindre l'extremum local (qu'on espère être à ce moment-là l'extremum
global).

Ici, la fonction à optimiser sera la vraisemblance L du texte. 
Partant du texte à déchiffrer, on va
appliquer l'algorithme suivant : 

-on réalise sur le texte une permutation circulaire de trois lettres de l'alphabet choisies au
hasard (par exemple, tous les 'a' deviennent des 't', tous les 't' deviennent des 'z' et
tous les 'z' deviennent des 'a'). 
On obtient ainsi un nouveau texte. 

-Si la vraisemblance L1 de ce nouveau texte est supérieure à celle du texte précédent (L0),
il devient le nouveau texte à déchiffrer. 

-Sinon, il peut devenir quand même le nouveau texte à déchiffrer, mais seulement avec la
probabilité ![equation](http://www.sciweavers.org/download/Tex2Img_1615582434.jpg) (critère de Metropolis).

Le paramètre Beta est inversement proportionnel au paramètre T évoqué plus haut. Il
croît donc au cours du temps selon une fonction à déterminer. Ici on choisit ![equation](http://www.sciweavers.org/download/Tex2Img_1615582624.jpg)
, avec i compteur d'itérations de l'algorithme.

Ne pas à hésiter à relancer plusieurs fois l'algorithme et éventuellement changer le nombre d'itérations, le résultat n'est pas toujours garanti.

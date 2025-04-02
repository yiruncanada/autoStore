# Projet proposé (Vous pouvez proposer votre propre projet):
Écrire un programme en
python qui permet de gérer un concessionnaire automobile. Toutes les opérations 
sur les autos ou les concessionnaires doivent etre faites
à travers des méthodes de la classe Concessionnaire, et il faut utiliser une classe
Auto pour représenter les autos. (Pour un défi extra, utiliser git pour historiser les
versions de votre projet au fur et à mesure).

- Les autos doivent avoir au moins une marque, prix, modele, couleur,kilométrage, des informations
sur le moteur comme capacité en Litres, le nombre de cylindres,
ou si c'est un moteur electrique. Le concessionnaire doit savoir à quel espace de stationnement
chaque auto est stationné (Vous pouvez simuler les espaces de
stationnement comme vous voulez dans le concessionnaire, par exemple vous pouvez programmer
un concessionnaire qui a 100 espaces de stationnement). 

- Le programme roule en continue et il est interactif, il donne les options essentielles
suivantes à l'usager:

1- voir tous les autos qui sont en inventaire
2- filtrer les autos sur des critères comme couleur, moteur, prix (intervalle),
    si moteur électrique
3- marquer un auto comme vendu, cet auto ne devra plus apparaître dans les recherches.
4- ajouter un auto
5- terminer le programme

Ajoutez n'importe quelle fonctionnalité extra que vous voulez.

Au démarrage, le programme doit créer le concessionaire et populer l'inventaire avec une
liste initiale d'autos différents.


---------------------------------------------------------------------------------------
- Défi: À la place de populer l'inventaire en créant directement des objets de type
Auto dans le code, populer l'inventaire à partir d'un fichier .json ou .txt
qui contient les caractéristiques des autos à initialiser.

- Défi : À la fermeture, le programme doit documenter tout son inventaire dans un fichier
.txt ou .json, ce qui permet de sauvegarder l'état des autos en inventaire pour ne pas
les perdre à l'arrêt du progamme.
# Projet informatique 2025 - Algorithme quarto

Cet algorithme permet de jouer au jeu quarto grâce au gestionnaire de partie https://github.com/qlurkin/PI2CChampionshipRunner.git.

## Stratégie

Avant de commencer, il vaut mieux de préciser que nous n'avons pas fait comme éxpliquer dans le cours, c'est a dire utiliser une heuristique. Nous avons décider de le faire de notre maniére mais il a plusieures incovenients, le plus grand étant que nous pouvons pas "regarder" dans le future. Il serait surement possible de le faire avec notre code mais nous n'avions pas asser de temps. Cependant, avec les matchs qu'on a fait avec nos amis, notre bot fonctionne quand même plutôt bien.


La stratégie utilisée pour permettre au bot de gagner ses parties est divisée en deux sections:
* Poser la pièce reçue
* Donner la pièce suivante

### Choisir la position de la pièce reçue

La position de la première pièce à placer est choisie aléatoirement.

On pose la pièce reçue sur une case et on regarde pour chaque ligne quelles pièces ont des caractéristiques en commun avec la pièce reçue. On vérifie pour chaque caractéristiques combien de fois elles sont en commun avec les caractéristiques de notre pièce reçue. 

Quand il y a quatre fois la même caractéristique en commun sur une ligne, c'est une ligne gagnante (la pièce reçue est comptée avec), donc on pose notre pièce à cet endroit.
Dans les autres cas, on place la pièce ou il y a le plus grand nombre d'une caractéristique en commun.

### Choisir la pièce à donner

La première pièce à donner est choisie aléatoirement.

Pour chaque pièce possible à jouer, pour chaque case, pour chaque ligne, on vérifie combien il y a de caractéristiques les mêmes en commun.

Si il y a quatre fois la même caractéristique en commun sur une ligne, on ne prend pas la piece en compte en faisant un break dans la boucle pour qu'elle ne soit pas choisie. On change aussi une variable de False à true pour être sur qu'elle ne soit pas choisie.

Pour les autres cas, on calcule de la même manière que pour la position de la pièce reçue mais ici la condition change et on renvoie une pièce et non une position .

## Bibliothèques utilisées

Nous avons utilisé les bibliothèques suivantes:
* random
* socket
* json
* copy
* time

### random

Nous avons utilisé random pour choisir la première pièce à donner et la position de la première pièce à placer.

### socket

Cette bibliothèque a été utilisée pour se connecter au gestionnaire de partie.

### json

Nous avons utilisé json pour envoyer et recevoir des informations du gestionnaire de partie.

### copy 

Copy nous a servi à copier le board pour ne pas modifier le board original.

### time

Le module time est utilisé dans le décorateur pour savoir combien de temps un bout de code a été exécuté.
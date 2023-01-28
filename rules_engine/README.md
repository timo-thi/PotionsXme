# Moteur de règles

L'objectif de cet exercice est d'écrire un moteur de règles pouvant interpréter des règles au format JSON. 

## Définitions

Une règle a toujours le même format, c'est un objet avec une seule clé en entrée. Cette clé correspond au nom de l'opération à effectuer. La valeur de la clé est un tableau avec tous les arguments nécéssaires à l'opération. Ces arguments peuvent être des règles ou des constantes. 

Exemple de règle 
```json
  {
    "operation_name": [operation_arguments]
  }
```

## Aide

Pour faire ce moteur de règles, tu dois utiliser une fonction récursive.  
Une fonction récursive est une fonction qui s'appelle elle-même.


## Format des entrées

Cet exercice est accompagné de 5 entrées différentes te permettant de tester ton code.  
Nous te conseillons de créer toi-même d'autres entrées pour tester des cas qui ne sont pas couverts par nos entrées.  

Les entrées ont toutes le même format : un objet JSON avec deux clés :
- input
  - context : le contexte sur lequel les règles doivent être appliquées
  - rule : la règle à appliquer
- output : la sortie attendue

### Input 1

Nouvelle règle :
- and : applique l'opérateur ET logique à deux variables

### Input 2

Nouvelle règle :
- var : récupère le contenu d'une variable dans le contexte des règles

### Input 3 :

Nouvelles règles :
- equals : vérifie que deux variables soient égales
- increment : incrémente une variable puis renvoie le résultat

### Input 4 (bonus) :

Nouvelles règles :
- lower_than : vérifie que la première variable soit inférieure à la seconde
- filter : filter les éléments d'une liste en fonction d'une règle
- prop : récupère un attribut de l'élément en cours

### Input 5 (bonus) :

Nouvelle règle :
- if : exécute et renvoie le résultat de la deuxième règle passée en paramètre si la condition de la première règle est validée ou de la troisième si la condition n'est pas validée

## Points importants

Ton code doit être documenté et respecter les bonnes pratiques du langage que tu as choisi. 

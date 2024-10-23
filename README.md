# Exemple d'utilisation du module Logging avec Python dans une application composé de plusieurs modules 

L'objectif de cet exemple est pédagogique et vise à montrer comment utiliser **le logging de la bibliothèque standard de Python** pour journaliser des informations, des erreurs, des avertissements. Il montre comment organiser la configuration du logger racine dans un fichier de config, ainsi que les loggers enfants dans chaque module de l'application. 

## Tester l'exemple

Cet exemple utilise uniquement la bibliothèque standard de Python. Il n'y a pas de dépendance installer.

Pour démarrer l'application, exécutez cette commande:
```bash
$ python -m exemple
```

Les logs avec un niveau DEBUG et plus haut vont dand le fichier exemple.log.
Les logd avec un noveau ERROR et plus haut sont en plus affichés sur le terminal.

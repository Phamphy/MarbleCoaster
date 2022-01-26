# Rollercoaster-Simulator

Sprints :


- 19/11 après-midi :
Creation d'une première demo simple avec seulement les fonctionnalitée strictements nécessaires +tests+clean code

répartition : un groupe gère l'interface graphique, l'autre le moteur physique sur pymunk

fonctionnalités : 

_ fichier pygame_interface.py gérant la communication avec l'utilisateur via l'interface graphique

    permettre à l'utilisateur de tracer la courbe
    
    permettre à l'utilisateur de choisir la position de départ de la bille
    
    transmettre ces données au programme fichier_pymunk.py
                  
_ fichier fichier_pymunk.py gérant la physique grâce à pymunk

    gérer les deplacements de la bille grâce à pymunk
    
    transmettre la position de la bille au programme pygame_interface.py

- 21/11 matin :
Amelioration de l'interface et affichage des données physiques (Ep, Ec, vitesse, hauteur, accélération ...) +tests+clean code

répartition : un groupe gère l'interface graphique, l'autre les données physiques

fonctionnalités : 

_ fichier pygame_interface.py gérant la communication avec l'utilisateur via l'interface graphique

    afficher en temps réel les données physiques
    
    à la fin de la simulation, afficher des graphiques résumant la simulation
                  
_ fichier donnees_physiques.py gérant la physique grâce à pymunk

    récupérer en temps réel des données du programme fichier_pymunk.py

    gérer les données physiques en temps réel
    
    communiquer ces données au programme pygame_interface.py

- 21/11 après-midi :
Commencer à rendre la simulation ludique (objectifs à atteindre, système de niveaux ...) +tests+clean code

répartition : un groupe gère l'implémentation de niveaux, l'autre les fonctionnalités ludiques

- 22/11 matin :
Continuer et finir le côté ludique +tests+clean code

répartition : pareil

- 23/11 matin :
Travail sur la présentation du projet

répartition : chacun travail sur une partie du code pour être capable de le présenter

- 23/11 après-midi :
Présentation du projet pour l'évaluation

répartition : tout le monde présente le projet pour l'évaluation


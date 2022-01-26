import pygame
from pygame.locals import *
import pymunk
from numpy import *
from math import *



def conversion_pixel_metre(valeur):
    """Fonction permettant de convertir les valeurs données en pixels en mètres"""
    return valeur * 0.0265


def obtenir_donnees_physiques(ball,bodyball, pos1, pos2):
    """retourne les donnes physiques utiles"""

    #temps entre deux appels de la fonction
    dt = 1/50

    # On calcule la vitesse convertie en mètre par seconde
    #v = int(sqrt((conversion_pixel_metre(pos2[0] - pos1[0])/dt)**2 + (conversion_pixel_metre(pos2[1] - pos1[1])/dt)**2))
    v=bodyball.velocity_at_world_point((0,0))
    # On calcule les énergies afin de les afficher à l'aide d'une nouvelle fonction
    vitesse=sqrt(v[0]**2+v[1]**2)
    energie_cinetique = 0.5 * ball.body.mass * vitesse**2
    #energie_potentielle = ball.body.mass * 9.81 * conversion_pixel_metre(700-pos2[1])
    energie_potentielle = ball.body.mass * 981 * (700-pos2[1])
    energie_mecanique = energie_cinetique + energie_potentielle

    return vitesse, energie_cinetique, energie_potentielle, energie_mecanique, int(700-pos2[1])


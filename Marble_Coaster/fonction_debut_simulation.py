import sys
import pygame
from pygame.locals import *
import pymunk
from numpy import *
from pymunk import Vec2d


def conversion_pymunk_pygame(Liste):
    """"Fonction convertissant les coordonnées pymunk en coordonnées pycharm et inversement"""
    n = len(Liste)
    Nouvelle_liste = []
    for i in range(n):
        Nouvelle_liste.append((Liste[i][0], 700 - Liste[i][1]))
    return Nouvelle_liste


def add_ball(space, position):
    """Ajoute une balle dans l'espace à une position donnée"""
    mass = 1
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = position
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    return shape,body


def position_balle(balle):
    """Donne la position de la balle en coordonnées corrigées"""
    return (balle.body.position.x,700-balle.body.position.y)

def destroy_ball(balle,bodyballe,espace):
    """detruit une balle de l'espace"""
    espace.remove(balle,bodyballe)


def add_obstacle(espace,x,y,largeur,hauteur):
    """ajoute un obstacle dans l'espace"""
    body_obstacle = pymunk.Body(body_type=pymunk.Body.STATIC)
    body_obstacle.position = (0,0)
    coordonnee=[(x,700-y),(x+largeur,700-y),(x+largeur,700-y-hauteur),(x,700-y-hauteur)]
    maForme_object=pymunk.Poly(body_obstacle,coordonnee)
    espace.add(body_obstacle, maForme_object)


def zone_de_boost(corpsballe, pos_balle_x, pos_balle_y, x, y, pos_boost_largeur, pos_boost_hauteur):
    """gere une zone de boost"""
    if x<pos_balle_x<x+pos_boost_largeur and y<pos_balle_y<y+pos_boost_hauteur:
        corpsballe.apply_impulse_at_local_point(Vec2d((0,50)))


def simulation_pymunk(Coordonnees_structure, position_initiale):
    """demarre la simulation physique sans l'affichage"""

    #on genere l'espace
    space = pymunk.Space()
    space.gravity = (0.0, -981)

    #on cree la balle physiquement
    position_initiale[1]=700-position_initiale[1]
    ball,bodyball = add_ball(space, position_initiale)

    #on caracterise la structure dessine par l'utilisateur
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 0)

    #On place la structure statique dessinée par l'utilisateur dans le modèle physique
    n = len(Coordonnees_structure)
    liste_coordonnees_pymunk = conversion_pymunk_pygame(Coordonnees_structure)

    #On affiche la structure à l'endroit sur pymunk
    for i in range(n-1):
        Ligne_pymunk = pymunk.Segment(body, liste_coordonnees_pymunk[i], liste_coordonnees_pymunk[i + 1], 5)
        #On trace la courbe dessinée par l'utilisateur dans le modèle physique
        space.add(Ligne_pymunk)

    return ball,space,bodyball


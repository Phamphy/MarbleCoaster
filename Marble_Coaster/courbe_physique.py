import sys
import pygame
from pygame.locals import *
import pymunk
from numpy import *

def conversion_pymunk_pygame(Liste):
    """Convertit les coordonnées pymunk en coordonnées pygame et inversement"""
    n = len(Liste)
    Nouvelle_liste = []
    for i in range(n):
        #On a choisi une interface de 700 pixels de hauteur, on convertit en remplaçant y par 700 - y
        Nouvelle_liste.append((Liste[i][0], 700 - Liste[i][1]))
    return Nouvelle_liste

def add_ball(space):
    mass = 1
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    x = random.randint(100, 600)
    #On place la balle sur une abscisse au hasard et en haut de la fenêtre
    body.position = x, 700
    shape = pymunk.Circle(body, radius)
    #On donne à la balle la forme d'un cercle
    space.add(body, shape)
    #On ajoute la balle à l'espace
    return shape

def draw_ball(screen, ball):
    """Dessine la balle sur la fenêtre pygame"""
    p = int(ball.body.position.x), 700 - int(ball.body.position.y)
    #On adapte le système de coordonnées
    pygame.draw.circle(screen, (0, 0, 255), p, int(ball.radius), 2)
    #On dessine la balle

def affichage_courbes_physiques(liste_coordonnees):
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    #Affichage de la fenêtre en résolution 1200x700
    pygame.display.set_caption(" Affichage jeu de la bille ")
    #Nom de la fenêtre
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -981)
    #On définit la gravité
    ball = add_ball(space)

    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (0, 0)
    #On définit l'origine

    n = len(liste_coordonnees)
    #Trace une courbe composée de n-1 segments à partir d'une liste de n coordonnées dans un modèle physique et un modèle affiché à l'écran
    liste_coordonnees_pymunk = conversion_pymunk_pygame(liste_coordonnees)
    Liste_lignes = []

    for i in range(n-1):
        Ligne_pymunk = pymunk.Segment(body, liste_coordonnees_pymunk[i], liste_coordonnees_pymunk[i + 1], 5)
        Ligne_pygame = pymunk.Segment(body, liste_coordonnees[i], liste_coordonnees[i + 1], 5)
        space.add(Ligne_pymunk)
        #Ajoute les segments à l'espace dans le modèle physique
        Liste_lignes.append(Ligne_pygame)
        #Ajoute les segments dans une liste que l'on affichera ensuite à l'écran

    while True:
        for event in pygame.event.get():
            #On quitte la fenêtre si on appuie sur echap ou la croix rouge
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        screen.fill((255, 255, 255))
        #Affiche la fenêtre en blanc

        for line in Liste_lignes:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            pygame.draw.lines(screen, (250, 2, 50), False, [pv1, pv2])
            #Dessine les lignes dans la fenêtre pygame

        draw_ball(screen, ball)

        space.step(1/50)
        #Met à jour l'espace
        pygame.display.flip()
        #On met à jour l'affichage
        clock.tick(50)
        #On attend 50 ms pour mettre à jour la position de la balle

liste_coordonnees = [[109, 111], [120, 125], [126, 136], [133, 147], [141, 159], [148, 170], [154, 182], [161, 193], [166, 204], [173, 216], [180, 227], [187, 238], [193, 249], [200, 261], [208, 275], [217, 289], [225, 300], [232, 311], [241, 322], [256, 336], [270, 349], [282, 360], [296, 377], [305, 388], [317, 400], [328, 409], [340, 423], [349, 435], [361, 446], [373, 457], [384, 470], [396, 481], [407, 492], [418, 504], [429, 511], [440, 517], [452, 520], [463, 521], [475, 520], [486, 518], [497, 518], [509, 516], [521, 511], [532, 505], [543, 502], [554, 499], [565, 495], [577, 487], [588, 478], [599, 470], [611, 462], [622, 452], [635, 442], [647, 435], [659, 423], [671, 411], [683, 404], [695, 392], [707, 377], [716, 366], [726, 353], [734, 342], [742, 330], [749, 319], [755, 308], [764, 294], [771, 280], [778, 267], [786, 256], [796, 241], [802, 230], [809, 219], [817, 203], [825, 190], [833, 178], [838, 166], [846, 155], [855, 142], [862, 131], [867, 119]]

if __name__ == '__main__':
    sys.exit(affichage_courbes_physiques(liste_coordonnees))





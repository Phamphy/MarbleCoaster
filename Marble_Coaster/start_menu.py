import pygame
from pygame.locals import *
from niveau1 import niveau1
from niveau2 import niveau2
from niveau3 import niveau3
from pygame_interface import modeLibre
from bouton import bouton

def niveau_1(fenetre,liste_boutons):
    """lancer le niveau 1"""
    for i in liste_boutons:
        i.desactiver()
    niveau1(fenetre)

def niveau_2(fenetre,liste_boutons):
    """lancer le niveau 2"""
    for i in liste_boutons:
        i.desactiver()
    niveau2(fenetre)

def niveau_3(fenetre,liste_boutons):
    """lancer le niveau 3"""
    for i in liste_boutons:
        i.desactiver()
    niveau3(fenetre,1)

def mode_libre(fenetre,liste_boutons):
    """lancer le mode libre"""
    for i in liste_boutons:
        i.desactiver()
    modeLibre(fenetre)

def quitter():
    """fermer la fenetre"""
    pygame.quit()

def titre(fenetre):
    """Affiche le titre"""
    myfont = pygame.font.SysFont("Comic sans MS", 100)
    label = myfont.render("MarbleCoaster",1,(255,0,0))
    text_rect = label.get_rect(center=(600, 50))
    fenetre.blit(label, text_rect)


def affichage_menu():
    """affiche la fenetre de menu"""

    #on créée une fenetre pygame
    pygame.init()
    fenetre = pygame.display.set_mode((1200,700))
    clock = pygame.time.Clock()

    #on cree les objets bouton
    bouton1=bouton(400,120,80,400,(200,0,0),(255,0,0),"Niveau 1",lambda:niveau_1(fenetre,liste_boutons))
    bouton2=bouton(400,220,80,400,(200,0,0),(255,0,0),"Niveau 2",lambda:niveau_2(fenetre,liste_boutons))
    bouton3=bouton(400,320,80,400,(200,0,0),(255,0,0),"Niveau 3",lambda:niveau_3(fenetre,liste_boutons))
    bouton4=bouton(400,420,80,400,(200,0,0),(255,0,0),"Mode libre",lambda:mode_libre(fenetre,liste_boutons))
    bouton5=bouton(400,550,80,400,(200,0,0),(255,0,0),"Quitter",quitter)
    liste_boutons=[bouton1,bouton2,bouton3,bouton4,bouton5]

    #on charge l'image de fond
    fond = pygame.image.load("Voie_lactee.jpg").convert()

    continuer=1

    #boucle gérant les évènements
    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT:
                #quitter la fenêtre
                continuer=0
                pygame.quit()
                break
            for i in liste_boutons:
                #on verifie si l'utilisateur clique sur un bouton
                i.clique(event,liste_boutons)

        for i in liste_boutons:
            #on active tous les boutons
            i.activer()

        #affichage du fond
        fenetre.blit(fond,(0,0))

        #on affiche le titre
        titre(fenetre)

        #afficher les boutons
        bouton1.afficher(fenetre)
        bouton2.afficher(fenetre)
        bouton3.afficher(fenetre)
        bouton4.afficher(fenetre)
        bouton5.afficher(fenetre)

        #mettre à jour l'affichage
        pygame.display.flip()
        clock.tick(50)


if __name__ == '__main__':
    affichage_menu()




affichage_menu()

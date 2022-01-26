import pygame
from pygame.locals import *
from fonction_debut_simulation import simulation_pymunk
from fonction_debut_simulation import position_balle
from affichage_physique import affichage_physique
from fonction_debut_simulation import destroy_ball



def resolution(liste,point,n=3):
    """fonction permettant de savoir si les coordonnées d'un point sont trop proches des coordonnées du dernier point d'une liste"""
    if len(liste)==0 :
        #si la liste est vide
        return True
    else :
        point_precedent=liste[-1]
        if abs(point_precedent[0]-point[0])<=n and abs(point_precedent[1]-point[1])<=n :
            #si le point est trop proche du point précédent
            return False
        else :
            #si le point est à bonne distance du point précédent
            return True


def afficher_ball(fenetre,pos_balle_x,pos_balle_y):
    """affiche la balle si elle ne sort pas des limite"""
    if 0<pos_balle_x<1200 and pos_balle_y<700:
        pygame.draw.circle(fenetre,(0,255,0),[int(pos_balle_x),int(pos_balle_y)],16)
        return True
    else :
        return False


def modeLibre(fenetre):

    clock = pygame.time.Clock()

    #definition de constantes utiles
    courbe = []
    continuer = 1
    x_mouse=0
    y_mouse=0
    pos1=0
    pos2=0
    balle_exist=True
    balle_physic_exist=False
    balle_destroyed=False
    fond = pygame.image.load("Voie_lactee.jpg").convert()
    #indique dans quelle séquence on se trouve (tracer de la courbe=1,position de la bille=2)
    sequence = 1


    #boucle gérant les évènements
    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT:
                #quitter la fenêtre
                continuer=0
                pygame.quit()
                break
            if event.type==MOUSEMOTION and event.buttons[0]==1 and sequence==1:
                #l'utilisateur trace une courbe en sequence 1
                if resolution(courbe,(event.pos[0],event.pos[1]),10):
                    courbe.append([event.pos[0],event.pos[1]])
            if event.type==MOUSEMOTION and sequence==2:
                #une bille suit le curseur en sequence 2
                x_mouse=event.pos[0]
                y_mouse=event.pos[1]
            if event.type==MOUSEBUTTONUP :
                #changement de séquence lorsque l'utilisateur lâche le clic gauche
                sequence+=1
                x_mouse=event.pos[0]
                y_mouse=event.pos[1]
            if event.type==MOUSEBUTTONDOWN and sequence==2 and event.button==1 :
                #on cree un espace physique pour commencer la simulation
                ball,space,bodyball=simulation_pymunk(courbe,[x_mouse,y_mouse])
                balle_physic_exist=True
                pos1=[x_mouse,y_mouse]
                pos2=pos1
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                #on revient au menu
                if not(balle_destroyed) and balle_physic_exist:
                    destroy_ball(ball,bodyball,space)
                continuer=0


        #affichage du fond
        fenetre.blit(fond,(0,0))

        if len(courbe)>1:
            #affichage de la courbe
            pygame.draw.lines(fenetre,(255,0,0),False,courbe,6)
        if sequence==2:
            #affichage de la bille en sequence 2
            pygame.draw.circle(fenetre,(0,255,0),[x_mouse,y_mouse],16)
        if sequence>=3 and balle_exist:
            #instruction a executer lors de la simulation
            pos=position_balle(ball)
            pos1=pos2
            pos2=pos
            affichage_physique(fenetre,ball,bodyball,pos1,pos2)
            space.step(1/50)
            balle_exist = afficher_ball(fenetre,int(pos[0]),int(pos[1]))


        if not(balle_exist) and not(balle_destroyed):
            #detruire le modele physique de la balle
            destroy_ball(ball,bodyball,space)
            balle_destroyed=True

        pygame.display.flip()
        clock.tick(50)










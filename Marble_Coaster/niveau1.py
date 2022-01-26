import pygame
from pygame.locals import *
from fonction_debut_simulation import simulation_pymunk
from fonction_debut_simulation import position_balle
from affichage_physique import affichage_physique
from affichage_physique import resultat
from fonction_debut_simulation import destroy_ball
from niveau2 import niveau2
from obtenir_donnees_physiques import obtenir_donnees_physiques



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


def zone_arrive(fenetre,x,y,image_arrive,pos_arrive_largeur,pos_arrive_hauteur,pos_balle_x,pos_balle_y):
    """gere la zone d'arrivee"""
    fenetre.blit(image_arrive,(x,y))
    if x<pos_balle_x<x+pos_arrive_largeur and y<pos_balle_y<y+pos_arrive_hauteur:
        #si la balle passe par la zone d'arrive
        return True
    else :
        return False


def afficher_victoire(fenetre):
    """affiche la victoire"""
    myfont = pygame.font.SysFont("freesansbold.ttf", 200)
    label = myfont.render("GAGNE !", 1, (255,255,255))
    text_rect = label.get_rect(center=(1200/2, 700/2))
    fenetre.blit(label, text_rect)


def afficher_defaite(fenetre):
    """affiche la defaite"""
    myfont = pygame.font.SysFont("freesansbold.ttf", 200)
    label = myfont.render("DEFAITE !", 1, (255,255,255))
    text_rect = label.get_rect(center=(1200/2, 700/2))
    fenetre.blit(label, text_rect)


def afficher_ball(fenetre,pos_balle_x,pos_balle_y):
    """affiche la balle si elle n'est pas sortie des limites"""
    if 0<pos_balle_x<1200 and pos_balle_y<700:
        pygame.draw.circle(fenetre,(0,255,0),[int(pos_balle_x),int(pos_balle_y)],16)
        return True
    else :
        return False

def afficher_tutoriel(fenetre):
    """afficher un petit tutoriel"""
    myfont = pygame.font.SysFont("freesansbold.ttf",24)
    tuto1 = "Cliquez longtemps en déplaçant la souris pour créer"
    tuto2 = "une rampe pour la bille afin qu'elle atteigne l'arrivée."
    tuto3 = "Attention la bille tombe dès que vous lâchez le bouton de la souris"
    tuto4 = "echap : revenir au menu"
    tuto5 = "espace : recommencer le niveau"
    label1 = myfont.render(tuto1, 1, (255,255,255))
    label2 = myfont.render(tuto2, 1, (255,255,255))
    label3 = myfont.render(tuto3, 1, (255,255,255))
    label4 = myfont.render(tuto4, 1, (255,255,255))
    label5 = myfont.render(tuto5, 1, (255,255,255))
    text_rect1 = label1.get_rect(center=(900,140))
    text_rect2 = label2.get_rect(center=(900,160))
    text_rect3 = label3.get_rect(center=(900,180))
    text_rect4 = label4.get_rect(center=(900,240))
    text_rect5 = label5.get_rect(center=(900,260))
    fenetre.blit(label1, text_rect1)
    fenetre.blit(label2, text_rect2)
    fenetre.blit(label3, text_rect3)
    fenetre.blit(label4, text_rect4)
    fenetre.blit(label5, text_rect5)



def niveau1(fenetre):
    """lance le niveau 1"""
    clock = pygame.time.Clock()

    #definition de constantes utiles
    courbe = []
    continuer = 1
    pos1=0
    pos2=0
    pos_balle_x=50
    pos_balle_y=50
    pos_arrive_x=1100
    pos_arrive_y=600
    pos_arrive_largeur=50
    pos_arrive_hauteur=50
    niveau_fini=False
    message_de_fin=False
    balle_exist=True
    balle_physic_exist=False
    balle_destroyed=False
    start_decompte=False
    afficher_tuto = True
    resultat_niveau_1 = resultat()
    decompte=0
    sequence = 1

    #chargement des images
    fond = pygame.image.load("Voie_lactee.jpg").convert()
    image_arrive = pygame.image.load("arrive.png").convert()
    image_arrive = pygame.transform.scale(image_arrive,(pos_arrive_largeur,pos_arrive_hauteur))

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
            if event.type==MOUSEBUTTONUP and sequence==1:
                #changement de séquence lorsque l'utilisateur lâche le clic gauche et debut de la simulation physique
                sequence+=1
                ball,space,bodyball=simulation_pymunk(courbe,[pos_balle_x,pos_balle_y])
                balle_physic_exist=True
                pos1=[pos_balle_x,pos_balle_y]
                pos2=pos1
                afficher_tuto = False
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                #si on clique sur la touche echappe, on quitte le niveau
                if not(balle_destroyed) and balle_physic_exist:
                    destroy_ball(ball,bodyball,space)
                continuer=0
            if event.type==KEYDOWN and event.key==K_SPACE:
                #si on clique sur la touche espace, on recommence le niveau
                if not(balle_destroyed) and balle_physic_exist:
                    destroy_ball(ball,bodyball,space)
                niveau1(fenetre)
                continuer=0

        #affichage du fond
        fenetre.blit(fond,(0,0))

        if len(courbe)>1:
            #affichage de la courbe dessine par l'utilisateur
            pygame.draw.lines(fenetre,(255,0,0),False,courbe,6)
        if afficher_tuto:
            #affiche le tutoriel
            afficher_tutoriel(fenetre)
        if sequence>=2 and balle_exist:
            #affiche les donnes physique dans le coin superieur droit
            pos=position_balle(ball)
            pos_balle_x=pos[0]
            pos_balle_y=pos[1]
            pos1=pos2
            pos2=pos
            affichage_physique(fenetre,ball,bodyball,pos1,pos2)
            v, Ec, Ep, Em,h=obtenir_donnees_physiques(ball,bodyball,pos1,pos2)
            resultat_niveau_1.ajouter_valeur(v,Ec,Ep,Em,h)
            #print(bodyball.velocity_at_world_point((0,0)))
            space.step(1/50)
        if niveau_fini:
            #si le niveau est reussi
            message_de_fin=True
        if message_de_fin:
            #on affiche le texte de victoire
            afficher_victoire(fenetre)
            start_decompte=True
        if not(balle_exist) and not(message_de_fin):
            #on affiche la defaite
            afficher_defaite(fenetre)
            start_decompte=True
        if start_decompte:
            #on effectue un decompte
            decompte+=1
        if decompte==200:
            #a la fin du decompte, on passe au niveau suivant
            if not(balle_destroyed):
                destroy_ball(ball,bodyball,space)
            if message_de_fin:
                resultat_niveau_1.courbe()
                niveau2(fenetre)
            continuer=0

        #on affiche la balle et la zone d'arrive
        niveau_fini = zone_arrive(fenetre,pos_arrive_x,pos_arrive_y,image_arrive,pos_arrive_largeur,pos_arrive_hauteur,pos_balle_x,pos_balle_y)
        balle_exist = afficher_ball(fenetre,pos_balle_x,pos_balle_y)

        #on detruit la balle si elle sort des limites
        if not(balle_exist) and not(balle_destroyed):
            destroy_ball(ball,bodyball,space)
            balle_destroyed=True

        #on met a jour l'affichage
        pygame.display.flip()
        clock.tick(50)






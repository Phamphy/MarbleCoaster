import pygame
from pygame.locals import *
from fonction_debut_simulation import simulation_pymunk
from fonction_debut_simulation import position_balle
from affichage_physique import affichage_physique
from affichage_physique import resultat
from obtenir_donnees_physiques import obtenir_donnees_physiques
from fonction_debut_simulation import destroy_ball
from fonction_debut_simulation import zone_de_boost


def afficher_zone_boost(fenetre,image_boost,x,y):
    """affiche la zone de boost"""
    fenetre.blit(image_boost, (x,y))


def afficher_message_echec(fenetre):
    """affiche un message educatif sur la conservation de l'energie"""
    myfont = pygame.font.SysFont("freesansbold.ttf",25)
    tuto1 = "Ce niveau est impossible : la balle n'a pas l'énergie nécessaire "
    tuto2 = "pour atteindre une zone plus haute que sa position initiale."
    tuto3 = "Pour réussir, il faut un apport d'énergie extérieur."
    label1 = myfont.render(tuto1, 1, (0,0,0))
    label2 = myfont.render(tuto2, 1, (0,0,0))
    label3 = myfont.render(tuto3, 1, (0,0,0))
    text_rect1 = label1.get_rect(center=(950,60))
    text_rect2 = label2.get_rect(center=(950,100))
    text_rect3 = label3.get_rect(center=(950,140))
    fenetre.blit(label1, text_rect1)
    fenetre.blit(label2, text_rect2)
    fenetre.blit(label3, text_rect3)


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
    """affiche la zone d'arrive et verifie si la balle y passe"""
    fenetre.blit(image_arrive,(x,y))
    if x<pos_balle_x<x+pos_arrive_largeur and y<pos_balle_y<y+pos_arrive_hauteur:
        return True
    else :
        return False


def afficher_victoire(fenetre):
    """afficher le texte de victoire"""
    myfont = pygame.font.SysFont("freesansbold.ttf", 200)
    label = myfont.render("GAGNE !", 1, (0,0,0))
    text_rect = label.get_rect(center=(1200/2, 700/2))
    fenetre.blit(label, text_rect)


def afficher_defaite(fenetre):
    """afficher le texte de defaite"""
    myfont = pygame.font.SysFont("freesansbold.ttf", 200)
    label = myfont.render("DEFAITE !",1,(0,0,0))
    text_rect = label.get_rect(center=(1200/2, 700/2))
    fenetre.blit(label, text_rect)


def afficher_ball(fenetre,pos_balle_x,pos_balle_y):
    """afficher la balle si elle est dans les limites"""
    if 0<pos_balle_x<1200 and pos_balle_y<700:
        pygame.draw.circle(fenetre,(0,255,0),[int(pos_balle_x),int(pos_balle_y)],16)
        return True
    else :
        return False


def niveau3(fenetre,nbr_lancer):
    """lance le niveau 3"""
    clock = pygame.time.Clock()

    #definition de constantes utiles
    courbe = []
    continuer = 1
    pos1=0
    pos2=0
    pos_balle_x=100
    pos_balle_y=300
    pos_arrive_x=1100
    pos_arrive_y=200
    pos_arrive_largeur=100
    pos_arrive_hauteur=100
    niveau_fini=False
    message_de_fin=False
    balle_exist=True
    balle_physic_exist=False
    balle_destroyed=False
    start_decompte=False
    afficher_message=True
    resultat_niveau_3 = resultat()
    compteur_echec = 0
    decompte=0
    sequence = 1

    #on charge les images utiles
    fond = pygame.image.load("renards.jpg").convert()
    fond = pygame.transform.scale(fond,(1200,900))
    image_arrive = pygame.image.load("arrive.png").convert()
    image_arrive = pygame.transform.scale(image_arrive,(pos_arrive_largeur,pos_arrive_hauteur))
    image_boost = pygame.image.load("fleche_haut.png").convert_alpha()
    image_boost = pygame.transform.scale(image_boost,(100,100))

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
                #changement de séquence lorsque l'utilisateur lâche le clic gauche et lancement de la simulation physique
                sequence+=1
                ball,space,bodyball=simulation_pymunk(courbe,[pos_balle_x,pos_balle_y])
                balle_physic_exist=True
                afficher_message=False
                pos1=[pos_balle_x,pos_balle_y]
                pos2=pos1
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                #si on clique sur la touche echap, on revient au menu
                if not(balle_destroyed) and balle_physic_exist:
                    destroy_ball(ball,bodyball,space)
                continuer=0
            if event.type==KEYDOWN and event.key==K_SPACE:
                #si on clique sur la touche espace, on recommence le niveau
                if not(balle_destroyed) and balle_physic_exist:
                    destroy_ball(ball,bodyball,space)
                niveau3(fenetre,nbr_lancer+1)
                continuer=0

        #affichage du fond
        fenetre.blit(fond,(0,0))

        if len(courbe)>1:
            #affichage de la courbe tracee par l'utilisateur
            pygame.draw.lines(fenetre,(255,0,0),False,courbe,6)
        if afficher_message and nbr_lancer==3:
            #afficher le message educatif
            afficher_message_echec(fenetre)
        if sequence>=2 and balle_exist:
            #affiche les donnes physiques dans le coin superieur droit
            pos=position_balle(ball)
            pos_balle_x=pos[0]
            pos_balle_y=pos[1]
            pos1=pos2
            pos2=pos
            affichage_physique(fenetre,ball,bodyball,pos1,pos2)
            v, Ec, Ep, Em,h = obtenir_donnees_physiques(ball,bodyball,pos1,pos2)
            resultat_niveau_3.ajouter_valeur(v,Ec,Ep,Em,h)
            if nbr_lancer>2:
                #on gere la zone de boost
                zone_de_boost(bodyball, pos_balle_x, pos_balle_y,900,350,100,100)
            space.step(1/50)
        if niveau_fini:
            #si on reussi le niveau
            message_de_fin=True
        if message_de_fin:
            #on affiche le texte de victoire
            afficher_victoire(fenetre)
            start_decompte=True
        if not(balle_exist) and not(message_de_fin):
            #on affiche le texte de defaite
            afficher_defaite(fenetre)
            compteur_echec += 1
            start_decompte=True
        if start_decompte:
            #on effectue un decompte
            decompte+=1
        if decompte==200:
            #lorsque le decompte est fini, on revient au menu
            if not(balle_destroyed):
                destroy_ball(ball,bodyball,space)
            if message_de_fin:
                resultat_niveau_3.courbe()
            continuer=0

        #on affiche la balle et la zone d'arrive
        niveau_fini = zone_arrive(fenetre,pos_arrive_x,pos_arrive_y,image_arrive,pos_arrive_largeur,pos_arrive_hauteur,pos_balle_x,pos_balle_y)
        balle_exist = afficher_ball(fenetre,pos_balle_x,pos_balle_y)
        if nbr_lancer>2:
            #on affiche la zone de boost
            afficher_zone_boost(fenetre,image_boost,900,350)

        #on detruit la balle si elle sort des limites
        if not(balle_exist) and not(balle_destroyed):
            destroy_ball(ball,bodyball,space)
            balle_destroyed=True

        #on met a jour l'affichage
        pygame.display.flip()
        clock.tick(50)









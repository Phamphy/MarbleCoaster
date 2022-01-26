import pygame
from pygame.locals import *


class bouton():

    def __init__(self,x,y,hauteur,largeur,couleur1,couleur2,texte,action):
        """creer un objet bouton"""
        self.x=x
        self.y=y
        self.hauteur=hauteur
        self.largeur=largeur
        self.couleur1=couleur1
        self.couleur2=couleur2
        self.texte=texte
        self.action=action
        self.actif=True

    def afficher(self,fenetre):
        """afficher le bouton dans une fenetre pygame"""
        mouse = pygame.mouse.get_pos()
        myfont = pygame.font.SysFont("freesansbold.ttf", 80)
        label = myfont.render(self.texte, 1, (255,255,255))
        if self.x<mouse[0]<self.x+self.largeur and self.y<mouse[1]<self.y+self.hauteur:
            #si le curseur est sur le bouton
            pygame.draw.rect(fenetre,self.couleur2,(self.x,self.y,self.largeur,self.hauteur))
        else :
            #si le curseur n'est pas sur le bouton
            pygame.draw.rect(fenetre,self.couleur1,(self.x,self.y,self.largeur,self.hauteur))
        text_rect = label.get_rect(center=(self.x+self.largeur/2, self.y+self.hauteur/2))
        fenetre.blit(label, text_rect)

    def clique(self,event,liste_boutons):
        """appelle une fonction lorsque l'on clique sur le bouton"""
        mouse = pygame.mouse.get_pos()
        if self.actif and self.x<mouse[0]<self.x+self.largeur and self.y<mouse[1]<self.y+self.hauteur:
            if event.type == MOUSEBUTTONUP:
                self.action()

    def desactiver(self):
        """desactiver le bouton"""
        self.actif=False

    def activer(self):
        """activer le bouton"""
        self.actif=True

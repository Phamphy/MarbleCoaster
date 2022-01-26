import pygame
from obtenir_donnees_physiques import obtenir_donnees_physiques
import matplotlib.pyplot as plt


def affichage_physique(fenetre,balle,bodyball,pos1,pos2) :
    """affiche les donnes physiques dans le coin superieur droit de l'ecran"""

    #on recupere les differentes valeurs utiles
    v,Ec,Ep,Em,h=obtenir_donnees_physiques(balle,bodyball,pos1,pos2)

    #on affiche les donnes
    pygame.draw.rect(fenetre,(255,0,0),(1100,20 + (1 - Ec/Em)*100,30,100*(Ec/Em)),0)
    pygame.draw.rect(fenetre,(0,255,0),(1150,20 + (1 - Ep/Em)*100,30,100*(Ep/Em)),0)

    vitesse = 'v= ' + str(int(v)) + 'pixels/s'
    font = pygame.font.SysFont("freesansbold.ttf", 40, bold = False, italic = False)
    texte = font.render(vitesse,1,(255,255,255))
    fenetre.blit(texte,(900,75))
    
    hauteur = 'h= ' + str(h) + 'pixels'
    texte = font.render(hauteur,1,(255,255,255))
    fenetre.blit(texte,(900,35))

    texte = font.render('Ec',1,(255,0,0))
    fenetre.blit(texte,(1100,130))

    texte = font.render('Ep',1,(0,255,0))
    fenetre.blit(texte,(1150,130))


class resultat():

    def __init__(self):
        self.vitesse=[]
        self.Ec=[]
        self.Ep=[]
        self.Em=[]
        self.hauteur=[]
        self.temps=[0]

    def ajouter_valeur(self,v,Ec,Ep,Em,hauteur):
        self.temps.append(self.temps[-1]+1/50)
        self.vitesse.append(v)
        self.Ec.append(Ec)
        self.Ep.append(Ep)
        self.Em.append(Em)
        self.hauteur.append(hauteur)

    def courbe(self):
        plt.subplot(311)
        plt.title("Vitesse")
        plt.plot(self.temps[:len(self.temps)-1],self.vitesse)
        plt.subplot(312)
        plt.title("Hauteur")
        plt.plot(self.temps[:len(self.temps)-1],self.hauteur)
        plt.subplot(313)
        plt.title("Energie")
        plt.plot(self.temps[:len(self.temps)-1],self.Ec,label="Ec")
        plt.plot(self.temps[:len(self.temps)-1],self.Ep,label="Ep")
        plt.plot(self.temps[:len(self.temps)-1],self.Em,label="Em")
        plt.legend()
        plt.show()




    
    
    
    
    

import pygame 
import random 
import math
import numpy as np

class Spillobjekt: 
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y 
        self.color = "gray"
        self.size = 15
        self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size*2, self.size*2)



class Bil(Spillobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.fart = 7
        self.color = "black"
        self.size = 10
        self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size*7, self.size*10)

    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size*7, self.size*10)

    def oppdater(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.fart 
        if keys[pygame.K_RIGHT]:
            self.x += self.fart 

class Linje: 
    def __init__ (self, h_x, h_y):
        self.x = h_x
        self.y = h_y
        self.b = 20
        self.h = 35
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)

    def oppdater(self):
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)


class Hinder:
    def __init__ (self, h_x, h_y):
        self.x = h_x
        self.y = h_y
        self.b = 20
        self.h = 35
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)

    def oppdater(self):
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)



pygame.init()

screen = pygame.display.set_mode((400, 500)) # Setter skjermen til 500x500 piksler.
clock = pygame.time.Clock()
running = True

bil = Bil(screen.get_width()/2, screen.get_height()/1.3)


linje = []
hinder = []

for x in range(5):
    spacing = np.linspace(0, screen.get_width(), 5)[x]
    linje.append(Linje(screen.get_width()/2 - 10, screen.get_height()/1000 + spacing))

for x in range(2):
    spacing2 = np.linspace(0, screen.get_width(), 2)[x]
    hinder.append(Hinder(screen.get_width()/4 - 10, screen.get_height()/1000 + spacing2))

while running:
    # Avslutter løkken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyller skjermen med hvit farge
    screen.fill("grey")    

    for x in linje:
        pygame.draw.rect(screen, "yellow", pygame.Rect(x.x, x.y, x.b, x.h))
        x.y += 5
        if x.y > screen.get_height(): 
            x.y = screen.get_width()/1000 
        x.oppdater()

    for x in hinder:
        pygame.draw.rect(screen, "yellow", pygame.Rect(x.x, x.y, x.b, x.h))
        x.y += 2
        if x.y > screen.get_height(): 
            x.y = screen.get_width()/1000 
        x.oppdater()

    bil.tegn()
    bil.oppdater()

     # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()

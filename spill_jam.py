import pygame 
import random as randint
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


class Søyle:
    def __init__ (self, sø_x, sø_y):
        self.x = sø_x
        self.y = sø_y
        self.h = randint(250, 400)
        self.b = 20
        self.rect = pygame.Rect(self.x, self.y, self.b, self.h)

    def oppdater(self):
        self.rect = pygame.Rect(self.x, self.y, self.b, self.h)


class Søyle2:
    def __init__(self, sø2x):
        self.x = sø2x
        self.y = randint(400, 500)
        self.h = 200
        self.b = 20
        self.rect = pygame.Rect(self.x, self.y, self.b, self.h)
    
    def oppdater(self):
        self.rect = pygame.Rect(self.x, self.y, self.b, self.h)



pygame.init()

screen = pygame.display.set_mode((400, 500)) # Setter skjermen til 500x500 piksler.
clock = pygame.time.Clock()
running = True

bil = Bil(screen.get_width()/2, screen.get_height()/1.3)

søyleliste = []
søyleliste2 = []

for a in range(4):
    spacing = np.linspace(0, screen.get_width(), 5)[a]
    søyleliste.append(Søyle(screen.get_width() + spacing, screen.get_height()/1000))

for b in range(4):
    spacing2 = np.linspace(0, screen.get_width(), 5)[b]
    søyleliste2.append(Søyle2(screen.get_width() + spacing2))

while running:
    # Avslutter løkken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyller skjermen med hvit farge
    screen.fill("grey")

    bil.tegn()
    bil.oppdater()    

     # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()

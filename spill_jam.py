import pygame
from random import randint  
import math
import numpy as np
import time 
from pygame import mixer

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
        self.size = 9
        self.image = pygame.image.load("bil.png")
        self.image = pygame.transform.scale(self.image, (self.size*7, self.size*10))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def tegn(self):
        screen.blit(self.image, self.rect.topleft)
        """
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size*7, self.size*10)
        """

    def oppdater(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (bil.x > screen.get_width() or bil.x > 0):
            self.x -= self.fart 
        if keys[pygame.K_RIGHT] and (bil.x < screen.get_width() or bil.x < 0):
            self.x += self.fart 
        self.rect = self.image.get_rect(center=(self.x, self.y))


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
        self.b = randint(10, 50)
        self.h = randint(10, 50)
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)

    def oppdater(self):
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)



pygame.init()

screen = pygame.display.set_mode((400, 500)) # Setter skjermen til 500x500 piksler.
clock = pygame.time.Clock()
mixer.music.load("Kavinsky - Nightcall (Drive Original Movie Soundtrack) (Official Audio).wav")
mixer.music.play(-1)

running = True
starting = True
ingame = False
slutt = False

#vei_rect = pygame.Rect(5,10, screen.get_width(), screen.get_height())

bil = Bil(screen.get_width()/2, screen.get_height()/1.3)


linje = []
hinder = []

#font = pygame.font.SysFont("Arial", int(screen.get_height()/30))
font_start = pygame.font.SysFont("Arial", 68)
font_start2 = pygame.font.SysFont("Arial", 32)
font_start3 = pygame.font.SysFont("Arial", 32)
font_start4 = pygame.font.SysFont("Arial", 32)

for x in range(5):
    spacing = np.linspace(0, screen.get_width(), 5)[x]
    linje.append(Linje(screen.get_width()/2 - 10, screen.get_height()/1000 + spacing))

for x in range(5):
    #spacing2 = np.linspace(0, screen.get_width(), 5)[x]
    hinder.append(Hinder(randint(10, screen.get_width()), -randint(10, 500)))

start_tid = time.time()

score = pygame.font.SysFont("arial", int(screen.get_height()/30))


while running:
    # Avslutter løkken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.key.get_pressed()[pygame.K_RETURN] and starting:
            print("gyvy")
            starting = False
            ingame = True
            inputword = ""
            break

        if pygame.key.get_pressed()[pygame.K_RETURN] and ingame == True:
            print("gyvy")
            starting = True
            slutt = False
            inputword = ""
            break

    # Fyller skjermen med hvit farge
    screen.fill("grey")  

    if starting: 
        # Skriver ut tittel på spillet 
        tekst_start = font_start.render("RACING", True, "blue")
        tekst_rect_start = tekst_start.get_rect(center = (screen.get_width()/2, screen.get_height()/3))
        screen.blit(tekst_start,tekst_rect_start)

        # Tegn press return for å starte start
        tekst_start2 = font_start2.render("Trykk 'enter' for å starte", True, "blue")
        tekst_rect_start2 = tekst_start2.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst_start2, tekst_rect_start2)

    if ingame:
        #if bil.x > screen.get_width() or bil.x < 0:
            #print("crash") 

        slutt_tid = round(time.time() - start_tid, 2)
        #print(slutt_tid)

        for x in linje:
            pygame.draw.rect(screen, "yellow", pygame.Rect(x.x, x.y, x.b, x.h))
            x.y += 5
            if x.y > screen.get_height(): 
                x.y = screen.get_width()/1000 
            x.oppdater()

        for x in hinder:
            pygame.draw.rect(screen, "red", pygame.Rect(x.x, x.y, x.b, x.h))
            x.y += 3
            if x.y > screen.get_height(): 
                x.y = screen.get_width()/1000 
                x.x = randint(10, screen.get_width())
            x.oppdater()

        bil.tegn()
        bil.oppdater()

        for x in hinder:
            if pygame.Rect.colliderect(x.rect, bil.rect):
                ingame = False 
                slutt = True

        tekst = score.render(str(slutt_tid), True, "black")
        tekst_rect = tekst.get_rect(center = (screen.get_width()/10, screen.get_height()/20))
        screen.blit(tekst, tekst_rect)

    
    if slutt: 
        # Skriver ut tittel på spillet 
        tekst_start3 = font_start3.render(f"di rekord: {score}", True, "blue")
        tekst_rect_start3 = tekst_start3.get_rect(center = (screen.get_width()/2, screen.get_height()/3))
        screen.blit(tekst_start3,tekst_rect_start3)

        # Tegn press return for å starte start
        tekst_start4 = font_start4.render("Trykk 'enter' for å gå til startsjerm", True, "blue")
        tekst_rect_start4 = tekst_start4.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst_start4, tekst_rect_start4)


    # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()

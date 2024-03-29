import pygame
from random import randint  
import math
import numpy as np
import time 
from pygame import mixer

# lager klasse spillobjekt 
class Spillobjekt: 
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y 
        self.color = "gray"
        self.size = 15
        self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size*2, self.size*2)


# lager klasse bil som arver fra klasse spillobjekt
class Bil(Spillobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.fart = 7
        self.size = 9
        self.image = pygame.image.load("bil.png") # setter bilde på bilen
        self.image = pygame.transform.scale(self.image, (self.size*7, self.size*10))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.hitbox = self.rect
        self.image_rect = self.image.get_rect(center=(self.x, self.y))
        self.motion_blur_images = []  
        self.max_blur_images = 4
        self.blur_offset = 3
 
 # tegner blure effekten på bilen
    def tegn(self):
        screen.blit(self.image, self.rect.topleft)
        for blur_image in self.motion_blur_images:
            screen.blit(blur_image[0], blur_image[1])

 # lager en funksjon for blur motion
    def update_motion_blur(self):
        self.motion_blur_images.append((self.image, self.rect.topleft))  
        if len(self.motion_blur_images) > self.max_blur_images:
            del self.motion_blur_images[0]  
    
# lager en oppdaterings funksjon som oppdaterers hver frame
    def oppdater(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (bil.x > screen.get_width() or bil.x > 0): 
            self.x -= self.fart 
        if keys[pygame.K_RIGHT] and (bil.x < screen.get_width() or bil.x < 0):
            self.x += self.fart 
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.hitbox = self.image.get_rect(center=(self.x + 2, self.y))
        self.hitbox = self.hitbox.scale_by(0.54)
        self.update_motion_blur()

        left_headlight_pos = (-11, -33)  # plasering for venstre hedlight
        right_headlight_pos = (11, -33)  # plasering for høyre hedlight
       
        left_headlight = (self.rect.centerx + left_headlight_pos[0], self.rect.centery + left_headlight_pos[1])
        right_headlight = (self.rect.centerx + right_headlight_pos[0], self.rect.centery + right_headlight_pos[1])
       
       # lager farge på lysene
        pygame.draw.circle(screen, (243, 255, 127), left_headlight, 3) 
        pygame.draw.circle(screen, (243, 255, 127), right_headlight, 3)

# lager en klasse fro varsellinjen (gul linje i midten av kjernemn)
class Linje: 
    def __init__ (self, h_x, h_y):
        self.x = h_x
        self.y = h_y
        self.b = 20
        self.h = 35
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)

    def oppdater(self):
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)

# lager en klasse for hindere (røde objekter)
class Hinder:
    def __init__ (self, h_x, h_y):
        self.x = h_x
        self.y = h_y
        self.b = randint(10, 50)
        self.h = randint(10, 50)
        self.fart_hinder = 3
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)

    def oppdater(self):
        self.rect = pygame.Rect(self.x - self.b/2, self.y, self.b, self.h)




pygame.init()

screen = pygame.display.set_mode((400, 500)) # Setter skjermen til 500x500 piksler.
clock = pygame.time.Clock()
mixer.music.load("Kavinsky - Nightcall (Drive Original Movie Soundtrack) (Official Audio).wav") # setter bakgrunnsmusikk
hitSound = pygame.mixer.Sound("crash.wav") # setter soundeffekt for kolisjon
hitSound.set_volume(1)
mixer.music.play(-1)

running = True
starting = True
ingame = False
slutt = False

#vei_rect = pygame.Rect(5,10, screen.get_width(), screen.get_height())

bil = Bil(screen.get_width()/2, screen.get_height()/1.3)




linje = []
hinder = []

# teksttyper på startkjerm
font_start = pygame.font.SysFont("Arial", 68)
font_start2 = pygame.font.SysFont("Arial", 32)
# teksttyper fro sluttkjerm
font_start3 = pygame.font.SysFont("Arial", 32)
font_start4 = pygame.font.SysFont("Arial", 32)

# lager varsellinje (gule linjer)
for x in range(5):
    spacing = np.linspace(0, screen.get_width(), 5)[x]
    linje.append(Linje(screen.get_width()/2 - 10, (screen.get_height()/1000) + spacing))

# lager hinder
for x in range(5):
    hinder.append(Hinder(randint(10, screen.get_width()), -randint(10, 500)))

# tid for score
start_tid = time.time()
teller_tid = 0

# tekst for score
score_font = pygame.font.SysFont("arial", int(screen.get_height()/30))

# Farger
vei_farge = pygame.Color((40,50,60))

while running:
    # Avslutter løkken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# if loop for å komme til sluttkjerm
        if pygame.key.get_pressed()[pygame.K_RETURN] and starting and (slutt == False):
            print("gyvy")
            starting = False
            slutt = False
            ingame = True
            inputword = ""
            start_tid = time.time()
            break

# if loop for å komme til startkjerm
        if pygame.key.get_pressed()[pygame.K_RETURN] and ingame == False:
            print("gyvy")
            starting = True
            slutt = False
            inputword = ""
            break

    # Fyller skjermen med hvit farge
    screen.fill(vei_farge)  


# startkjerm
    if starting: 
        # Skriver ut tittel på spillet 
        tekst_start = font_start.render("RACING", True, "blue")
        tekst_rect_start = tekst_start.get_rect(center = (screen.get_width()/2, screen.get_height()/3))
        screen.blit(tekst_start,tekst_rect_start)

        # Tegn press return for å starte start
        tekst_start2 = font_start2.render("Trykk 'enter' for å starte", True, "blue")
        tekst_rect_start2 = tekst_start2.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst_start2, tekst_rect_start2)

#spillekjerm / ingame kjerm
    if ingame:
        #if bil.x > screen.get_width() or bil.x < 0:
            #print("crash") 

        slutt_tid = round(time.time() - start_tid, 2)
        #print(slutt_tid)

# setter bevegelse på de gule linjene
        for x in linje:
            pygame.draw.rect(screen, "yellow", x.rect)
            x.y += 5
            if x.y > screen.get_height(): 
                x.y = screen.get_width()/1000
            x.oppdater()

# setter bevegelse på hinder (røde objekter)
        for x in hinder:
            pygame.draw.rect(screen, "red", x.rect)
            x.y += x.fart_hinder
            if x.y > screen.get_height(): 
                x.y = screen.get_width()/1000
                x.x = randint(10, screen.get_width())
            x.oppdater()

# tegner bil og oppdaterer bevegelse og funksjon på bil
        bil.tegn()
        bil.oppdater()

# if setning for at objektene vil falle med += 1 per 3 sek, og bilens fart += 0.5 per 3 sek
        if (time.time() - teller_tid) >= 3:
            for x in hinder:
                x.fart_hinder += 1
            bil.fart += 0.5
            teller_tid = time.time()

# if setning fro kolisjon mellom bil og hinder         
        for x in hinder:
            if pygame.Rect.colliderect(x.rect, bil.hitbox):
                for x in hinder:
                    x.y = -randint(10, 500)
                    x.x = randint(10, screen.get_width())
                    x.fart_hinder = 3
                bil = Bil(screen.get_width()/2, screen.get_height()/1.3)
                pygame.mixer.Sound.play(hitSound) # spiller lydefeekten for kolisjon
                ingame = False 
                slutt = True
                tid = slutt_tid
                    
# skriver scor på ingame kjermen 
        tekst = score_font.render(str(slutt_tid), True, "grey")
        tekst_rect = tekst.get_rect(center = (screen.get_width()/10, screen.get_height()/20))
        screen.blit(tekst, tekst_rect)

# sluttkjerm    
    if slutt: 
        # Skriver ut tittel på spillet 
        tekst_start3 = font_start3.render(f"Du tapte, din score ble: {round(tid, 2)} sek", True, "blue")
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

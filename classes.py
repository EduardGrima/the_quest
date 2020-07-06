import pygame 
from pygame.locals import *
import sys, random, os, _config
from main import *

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # metodos sprite rect, centerx, centery, Bottom(lado inferior), top(lado superior)
        # self.image = pygame.Surface((73,96), pygame.SRCALPHA, 32)
        self.image= pygame.image.load("resouces/images/player.png").convert() #mirar metodos convert
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 30
        self.rect.centery = 600 //2 
        self.vy = 0
        self.vx = 0
        self.vida = 100
        

    def update(self):
        self.vy = 0
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_DOWN]:
            self.vy = 5
        if keypressed[pygame.K_UP]:
            self.vy = -5 
        self.rect.y += self.vy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def updateX(self):
        self.vx = 8
        self.rect.x += self.vx



   

    def draw_vida_bar(self, surface, x, y, porciento):
        BAR_LARGO = 100
        BAR_ANCHO = 10
        fill = int((porciento /100)* BAR_LARGO)
        borde = pygame.Rect(x, y, BAR_LARGO, BAR_ANCHO)
        fill = pygame.Rect(x, y, fill, BAR_ANCHO)
        pygame.draw.rect(surface, GREEN, fill)
        pygame.draw.rect(surface, WHITE, borde, 2)
        


        
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resouces/images/meteorGrey_med1.png").convert() # mirar metodos convert
        self.image.set_colorkey(BACKGRAUND)
        self.rect = self.image.get_rect()
        self.__vx = 0
        self.reset()
        
        # self.vy = random.randrange(-3, 3) # si queremos movimiento diagonal

    def update(self):
        self.rect.x += self.vx
        # self.rect.y += self.vy
        if self.rect.left < 0:
            self.vx = 0
           
    
    def reset(self):
        self.rect.x = random.randrange(840 , 940)
        self.rect.y = random.randrange(0 , HEIGHT)
        self.vx = random.randrange(-7,-4) # El negativo mas pequeño a la izquierda me he vuelto loco!!!

    


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center): # center para pasar la posicion meteorito que ha colisionado
        self.anim_explosion = []
        
        for i in range(9):
            file ="./resouces/images/regularExplosion0{}.png".format(i)
            img = pygame.image.load(file).convert()
            img.set_colorkey(BACKGRAUND)
            img_scale = pygame.transform.scale(img, (70,70))
            self.anim_explosion.append(img_scale)

        super().__init__()
        self.image = self.anim_explosion[0]
        self.rect = self.image.get_rect()
        self.rect.center = center 
        self.frame = 0
        self.tiempo = pygame.time.get_ticks()
        self.frame_rate = 80 # controlar velocidad explosion

    def update(self):
        tiempo_nuevo = pygame.time.get_ticks()
        if tiempo_nuevo - self.tiempo > self.frame_rate:
            self.tiempo = tiempo_nuevo
            self.frame +=1
            if self.frame == len(self.anim_explosion):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.anim_explosion[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

         



class Planeta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("./resouces/images/planeta.jpg").convert()
        img_scale = pygame.transform.scale(img, (700,500))
        self.image= img_scale
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 800
        self.rect.centery = 600 //2 
        self.vx = 0

    def update(self):
        self.vx = -1
        
        self.rect.centerx += self.vx
        
        



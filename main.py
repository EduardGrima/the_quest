import pygame as pg
from pygame.locals import *
import sys, random

BACKGRAUND = (0,0,0)
YELLOW = (255, 255, 0)
WHITE= (255, 213, 126)

class Nave:
    def __init__(self):
        self.vy = 0
        self.vx = 0
        self.w =60
        self.h =20 
        self.Cx = 35
        self.Cy = 300

        self.image = pg.Surface((self.w, self.h))
        self.image.fill(WHITE)

    @property
    def posx(self):
        return self.Cx - self.w //2
    
    @property
    def posy(self):
        return self.Cy - self.h // 2

    def move(self, limSupX, limSubY):
        
        self.Cx += self.vx
        self.Cy += self.vy

        if self.Cy < self.h //2:
            self.Cy = self.h //2

        if self.Cy > limSubY:
            self.Cy = limSubY - self.h // 2 

    

class meteorito:
    def  __init__(self):
        self.vx = -0.5
        self.Cx = 800
        self.Cy = 300
        self.h = 40
        self.w = 40
        self.image  = pg.Surface((self.w,self.h))
        self.image.fill(YELLOW)

        

    @property
    def posx(self):
        return self.Cx - self.w //2
    
    @property
    def posy(self):
        return self.Cy - self.h // 2

    def move(self, limSupX, limSupY):
        if  self.Cx <= 0:
            self.Cx = limSupX
            self.Cy = random.randint(0, 600)
            
        else:
            self.Cx += self.vx
    

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800,600))
        self.pantalla.fill(BACKGRAUND)
        pg.display.set_caption("The_quest")
        self.meteo1 = meteorito()
        self.meteo2 = meteorito()
        self.meteo3 = meteorito()
        self.meteo4 = meteorito()
        self.apolo = Nave()
        

    def main_loop(self):
        game_over = False   

        while not game_over:
            for event in pg.event.get():
                if event.type == QUIT:
                    game_over = True

                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.apolo.vy = -0.5
                    if event.key == K_DOWN:
                        self.apolo.vy = 0.5

            key_pressed =pg.key.get_pressed()
            if key_pressed[K_UP]:
                self.apolo.vy = -2
            elif key_pressed[K_DOWN]:
                self.apolo.vy = 2
            else:
                self.apolo.vy = 0
            
            self.pantalla.fill(BACKGRAUND)   
            
            self.pantalla.blit(self.meteo1.image, (self.meteo1.posx, self.meteo1.posy))
            self.pantalla.blit(self.meteo2.image, (self.meteo2.posx, self.meteo2.posy))
            self.pantalla.blit(self.meteo3.image, (self.meteo3.posx, self.meteo3.posy))
            self.pantalla.blit(self.meteo4.image, (self.meteo4.posx, self.meteo4.posy))
            self.pantalla.blit(self.apolo.image, (self.apolo.posx, self.apolo.posy))
            self.meteo1.move(800, 600)
            self.meteo2.move(800, 600)
            self.meteo3.move(800, 600)
            self.meteo4.move(800, 600)
            self.apolo.move(800, 600)
            pg.display.flip()


    def quit(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()

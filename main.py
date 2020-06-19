import pygame as pg
from pygame.locals import *
import sys

BACKGRAUND = (0,0,0)
YELLOW = (255, 255, 0)

class Nave:
    pass

class Meteorito:
    def  __init__(self):
        self.vx = -5
        self.Cx = 800
        self.Cy = 300
        self.h = 40
        self.w = 40
        self.posx = self.Cx - self.w //2
        self.posy = self.Cy - self.h // 2


        self.image  = pg.Surface((40,40))
        self.image.fill(YELLOW)

        


class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800,600))
        self.pantalla.fill(BACKGRAUND)
        pg.display.set_caption("The_quest")
        self.meteo = Meteorito()

    def main_loop(self):
        game_over = False   

        while not game_over:
            for event in pg.event.get():
                if event.type == QUIT:
                    game_over = True
                

            self.pantalla.blit(self.meteo.image, (self.meteo.posx, self.meteo.posy))
            pg.display.flip()


    def quit(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()

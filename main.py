import pygame 
from pygame.locals import *
import sqlite3
import sys, random, os
from classes import *
from _config import BASE_DATOS



WIDTH = 800
HEIGHT = 600
BACKGRAUND = (0,0,0)
GREEN = (0, 255, 0)
WHITE= (255, 255, 255)

FPS = 60

CONFIGLEVEL={
    'LEVEL1': (5, (-6,-4),30), 
    'LEVEL2': (8, (-7, -5),50),
    'LEVEL3': (11, (-11, -8),60)
}

# pygame.mixer.init()

pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()

pygame.mixer.music.load('./resouces/sounds/music.ogg')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

sonido_Explosion = pygame.mixer.Sound('./resouces/sounds/explosion.wav')

class Game:
    def __init__(self):
        
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        self.pantalla.fill(BACKGRAUND)
        self.fondo= pygame.image.load("resouces/images/background.png")
        self.escore = 0
        self.font = pygame.font.Font("./resouces/fonts/font.ttf", 36)
        self.marcador = self.font.render(str(self.escore), True, WHITE)
        self.n_Player ='EDU'
        self.levelActual = 1
        
    def draw_text(self, surface, text, size, x, y):
        font = pygame.font.Font("./resouces/fonts/font.ttf", size)
        text_surface = font.render(text, False, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

         
    def entradaNombre(self):
        self.nombre =''
        introducir = True
        while introducir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == KEYUP:
                    if event.key == K_SPACE and len(self.nombre) >=3:
                        introducir = False
                    if len(self.nombre) <= 2:
                        self.nombre += str.upper(chr(event.key))
                    if event.key == K_DELETE:
                        x = len(self.nombre)
                        self.nombre = self.nombre[:-x]
                self.n_Player= self.nombre
                    
                
                        
                self.draw_text(self.pantalla, self.nombre, 35, WIDTH//2, HEIGHT * 4/5)    
                pygame.display.flip()


    
    def waiting(self):
        waiting = True
        while waiting:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        waiting = False

    def records_sqlite3(self):
        datos = (self.n_Player, self.escore)
        conn = sqlite3.connect(BASE_DATOS)
        cur = conn.cursor()

        query = 'INSERT into records (player, puntuacion) values (?, ?); '
        try:
            cur.execute(query, datos).fetchall()
                
        except sqlite3.Error:
            pass
        conn.commit()
        conn.close()

        conn = sqlite3.connect(BASE_DATOS)
        cur = conn.cursor()

        query ="SELECT id , player, puntuacion FROM records;"
        self.playersRecords = cur.execute(query).fetchall()
        conn.close()

        self.listaordenada = sorted(self.playersRecords, key=lambda x: x[2] ,reverse=True)
        #eliminar ultimo elemento si lista es mayor de len 2
        
        conn = sqlite3.connect(BASE_DATOS)
        cur = conn.cursor()
        query = "UPDATE records SET player =?, puntuacion=? where id = ?; "
        ids= 1
        for i in self.listaordenada:
            datos = i[1],i[2],ids
            cur.execute(query, datos)
            conn.commit()
            ids+= 1
        query =""
        conn.close()
        # Eliminar ultimo registro bases de datos
        if len(self.listaordenada)>3:
            query = "DELETE from records WHERE id= ?;"
            dato = (self.listaordenada[3][0],)
            conn = sqlite3.connect(BASE_DATOS)
            cur = conn.cursor()
            cur.execute(query,dato)
            conn.commit()
            conn.close() 

        
        return self.listaordenada
        
    
            
    
    def pantalla_Inicio(self):
        self.draw_text(self.pantalla, "The_Quest", 60, WIDTH //2 , HEIGHT //8 )
        self.draw_text(self.pantalla, "No choque con los meteoritos ", 35, WIDTH//2, HEIGHT //4)
        self.draw_text(self.pantalla, "Introduduzca sus iniciales y ", 35 , WIDTH//2, HEIGHT //2)
        self.draw_text(self.pantalla, "pulse espacio para continuar", 35 , WIDTH//2, HEIGHT * 3/5)
         
        self.entradaNombre()
        
        pygame.display.flip()
        self.waiting()

    
    def pantallaNivel(self):
        self.pantalla.blit(self.fondo, (0,0))
        self.draw_text(self.pantalla, str(self.escore), 50, WIDTH//2, HEIGHT //6)
        self.draw_text(self.pantalla, "FIN DE NIVEL {}".format(str(self.levelActual)), 50, WIDTH//2, HEIGHT //2)
        self.draw_text(self.pantalla, 'Pulse espacio para continuar', 50, WIDTH//2, HEIGHT //2+50)
        
        pygame.display.flip()
        self.waiting()               
   

    def pantalla_Game_Over(self):
        lista_recorsds = self.records_sqlite3()
        (lista_recorsds[0][2], lista_recorsds[1][2], lista_recorsds[2][2])
        self.pantalla.blit(self.fondo, (0,0))
        self.draw_text(self.pantalla,"{} su puntiacion: {}".format(self.n_Player ,str(self.escore)), 40, WIDTH//2, 90)
        self.draw_text(self.pantalla, "RECORDS", 40, WIDTH//2,  150)
        self.draw_text(self.pantalla,"NOMBRE  ",30, 300, 200 )
        self.draw_text(self.pantalla, "puntuacion", 30, 500, 200 )
        self.draw_text(self.pantalla, lista_recorsds[0][1],30, 300, 250 )
        self.draw_text(self.pantalla, lista_recorsds[0][2], 30, 500, 250 )
        self.draw_text(self.pantalla, lista_recorsds[1][1],30, 300, 300 )
        self.draw_text(self.pantalla, lista_recorsds[1][2], 30, 500, 300 )
        self.draw_text(self.pantalla, lista_recorsds[2][1],30, 300, 350 )
        self.draw_text(self.pantalla, lista_recorsds[2][2], 30, 500, 350 )
        
        
        pygame.display.flip()
        self.waiting()

   
    def main_loop(self):
            
            game_over = False
            iniciando = True
            jugando = True
            contador = 0
            
             

            while jugando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit()

                self.level = 'LEVEL{}'.format(str(self.levelActual))                              
                if iniciando:
                    self.pantalla.blit(self.fondo, (0,0))
                    if self.levelActual == 1:
                        self.escore = 0
                        self.pantalla_Inicio()
                                        
                    iniciando = False

                    self.apolo = Nave()
                    self.all_sprites = pygame.sprite.Group()
                    self.all_sprites.add(self.apolo)
                    self.meteor_list = pygame.sprite.Group()
                    for i in range(CONFIGLEVEL[self.level][0]):
                        self.meteor= Meteor()
                        self.meteor_list.add(self.meteor)
                        # falta propiedad para graduar velocidad meteor segun tupla y constante
                    
                    
                
                if contador >= CONFIGLEVEL[self.level][2]:
                    self.meteor_list.empty()
                    self.escore += int(self.apolo.vida)
                    iniciando = True
                    contador = 0
                    
                    self.planet= Planeta()
                    self.all_sprites.add(self.planet)
                    
                    completado = False
                    while not completado:
                        self.pantalla.blit(self.fondo, (0,0))
                        self.planet.update()
                        self.apolo.updateX()
                        self.all_sprites.draw(self.pantalla)
                        pygame.display.flip()
                        
                        if self.planet.rect.centerx <= 750:
                            completado = True
                            self.draw_text(self.pantalla, 'Pulse espacio para continuar', 50, WIDTH//2, HEIGHT //2)  
                            pygame.display.flip()
                            self.waiting() 
                    if self.levelActual  < 3:
                        self.pantallaNivel()
                        self.levelActual +=1         
                        
                    else:
                        self.levelActual = 1
                        game_over = True
                
                if game_over:
                    game_over= False
                    iniciando = True
                    self.pantalla_Game_Over()
               
                               
                self.all_sprites.update()
                self.meteor_list.update()
                for meteor in self.meteor_list:
                    if meteor.vx == 0:
                        self.escore += 1
                        self.marcador = self.font.render(str(self.escore), True, WHITE)
                        contador += 1
                        meteor.reset()
                        # falta propiedad para graduar velocidad meteor segun tupla y constante
                meteor_hit_list = pygame.sprite.spritecollide(self.apolo, self.meteor_list, True)       
                for meteor in meteor_hit_list:
                    self.escore -= 5
                    self.apolo.vida -= 10
                    self.explosion = Explosion(meteor.rect.center)
                    self.all_sprites.add(self.explosion)
                    sonido_Explosion.play()
                    self.meteor= Meteor()
                    # falta propiedad para graduar velocidad meteor segun tupla y constante
                    self.meteor_list.add(self.meteor)
                    self.all_sprites.add(self.meteor)
                    if self.apolo.vida <= 0:
                        game_over = True

                self.apolo.update()
                                               
                self.pantalla.blit(self.fondo, (0,0))
                self.pantalla.blit(self.marcador, (740, 10))
                self.meteor_list.draw(self.pantalla)
                self.all_sprites.draw(self.pantalla)
                self.apolo.draw_vida_bar(self.pantalla, 5, 5, self.apolo.vida)
                                               
                pygame.display.flip()
                clock.tick(FPS)

    def quit(self):
        pygame.quit()
        sys.exit()


if  __name__ == "__main__":
    pygame.init()
    game= Game()
    game.main_loop()
    game.quit()


    















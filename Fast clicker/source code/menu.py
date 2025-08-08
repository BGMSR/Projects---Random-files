import pygame
from random import randint
import time
from game import run_game
pygame.mixer.init()
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Fast Clicker")
BLUE = (71, 179, 225)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLACK = (0,0,0)
WHITE = (255,255,255)
window.fill(BLUE)
clock = pygame.time.Clock()
#Classes
class Area :
    def __init__(self,color,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def set_color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self,tickness,color):
        pygame.draw.rect(window,color,self.rect,tickness)
    def inclusion(self,x,y):
        return self.rect.collidepoint(x, y)
class Label(Area):
    def set_text(self, text, f_size, text_color):
        main_font = pygame.font.SysFont('veranda',f_size)
        self.image = main_font.render(text,True,text_color)
    def draw(self,shift_x,shift_y):
        self.fill()
        window.blit(self.image,(self.rect.x+shift_x,self.rect.y+shift_y))
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,picture,x,y,w,h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Button(Gamesprite):
    def pressed(self,x,y):
        return self.rect.collidepoint(x,y)
    def grow(self,factor,picture):
        w = int(self.rect.w * factor)
        h = int(self.rect.h * factor)
        self.image = pygame.transform.scale(pygame.image.load(picture),(w,h))
        self.rect = self.image.get_rect(center = self.rect.center)
welcome = Label(BLUE,125,20,50,50)
welcome.set_text('Welcome to Fast Clicker',30,WHITE)
welcome.draw(0,0)
play_butt = Button('Play button.png',140,90,200,90)
play_butt.reset()
exit_butt = Button('Exit button.png',140,270,200,90)
exit_butt.reset()
pop_sound = pygame.mixer.Sound("pop.mp3")
play = True
while play:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            x,y = e.pos
            if exit_butt.pressed(x,y) == True:
                pop_sound.play()
                exit_butt.grow(2,'Exit button.png')
                pygame.time.delay(500)
                play = False
            if play_butt.pressed(x,y) == True:
                pop_sound.play()
                run_game()
    pygame.display.update()
    clock.tick(40)
pygame.display.update()
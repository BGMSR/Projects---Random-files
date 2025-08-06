import pygame
from random import randint
import time
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Fast Clicker")
BLUE = (71, 179, 225)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLACK = (0,0,0)
window.fill(BLUE)
clock = pygame.time.Clock()
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
    def set_text(self, text, f_size, text_color=(0,0,0)):
        main_font = pygame.font.SysFont('veranda',f_size)
        self.image = main_font.render(text,True,text_color)
    def draw(self,shift_x,shift_y):
        self.fill()
        window.blit(self.image,(self.rect.x+shift_x,self.rect.y+shift_y))
#Creating cards
cards = []
x = 70
for i in range(4):
    card = Label(YELLOW,x,170,70,100)
    card.fill()
    card.outline(5,DARK_BLUE)
    card.set_text('CLICK',27)
    cards.append(card)
    x+=100
start_time = time.time()
cur_time = start_time
time_text = Label(BLUE,0,0,50,50)
time_text.set_text('Time',45)
time_text.draw(12,12)
timer = Label(BLUE,45,55,50,40)
timer.set_text(str(0),40)
timer.draw(0,0)
point_text = Label(BLUE,380,0,50,50)
pt = 0
point_text.set_text('Points',45)
point_text.draw(0,12)
points = Label(BLUE,445,55,50,40)
points.set_text(str(pt),40)
points.draw(0,0)
wait = 0
play = True
while play:
    new_time = time.time()
    timer.set_text(str(int(new_time - cur_time)),40,DARK_BLUE)
    timer.draw(0,0)
    if wait == 0:
        n = randint(0,3)
        for i in range(4):
            cards[i].set_color(YELLOW)
            if i == n:
                cards[i].draw(7,38)
                cards[i].outline(5,DARK_BLUE)
            else:
                cards[i].fill()
                cards[i].outline(5,DARK_BLUE)
        wait = 20
    else:
        wait -= 1
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                for i in range(4):
                    if cards[i].inclusion(x,y) == True:
                        if i == n:
                            cards[i].set_color(GREEN)
                            pt += 1
                        else:
                            cards[i].set_color(RED)
                        cards[i].fill()
                        points.set_text(str(pt),40)
                        points.draw(0,0)
                if pt == 5 and new_time - cur_time <= 10 :
                    win = Label(GREEN,0,0,500,500)
                    win.set_text('You win !',30)
                    win.draw(170,200)
                if new_time - cur_time > 11:
                    lose = Label(RED,0,0,500,500)
                    lose.set_text('You lost !',30)
                    lose.draw(170,200)
    pygame.display.update()
    clock.tick(40)
pygame.display.update()
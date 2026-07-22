import pygame
#from time import *
#from random import *
pygame.init()

window = pygame.display.set_mode(500,500)
clock = pygame.time.Clock()
back = (200, 250, 255)
window.fill(back)

class Area():
    def __init__(self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = back
        if color:
           self.fill_color = color

    def collide_point(self,x,y):
        return self.rect.collidepoint(x,y)

    def set_color(self,new_color): # а у нас тут должен быть return?
        self.fill_color = new_color
        #return self.new_color

    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)

    def outline(self,frame_color,thickness): # второй параметр это frame_color, но по идеи должен же быть fill_color
        pygame.draw.rect(window, self.fill_color, self.rect, thickness) # последнее за цвет (thickness)

    def collide_rect(self,rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self,filename,x,y,width,height):
        super().__init__(x,y,width,height,color = None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

ball = Picture('ball.png',250,250,50,50)
platform = Picture('platform.png',225,400,100,30)
start_x = 5
start_y = 5
monsters = list()
n = 9
for j in range(3):
    y = start_y + (55 * j) #координата монстра в каждом след. столбце будет смещена на 55 пикселей по y
    x = start_x + (27.5 * j) #и 27.5 по x
    for i in range(n):
        monster = Picture('enemy.png',x,y,50,50)
        monsters.append(monster)
        x += 55
    n -= 1

move_right = False
move_left = False

speed_x = 3
speed_y = 3
while True:
    window.fill(back)
    for monster in monsters:
        monster.draw()
    ball.fill()
    ball.draw()
    platform.fill()
    platform.draw()
    

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.colliderect(platform.rect):
        speed_y *= -1
        ball.rect.bottom = platform.rect.top


    if ball.rect.y < 0:
        speed_y *= -1
    
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1

    if ball.rect.y > 450:
        break

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right: # тоже самое что move_right == True:
        platform.rect.x += 3

    if move_left: # тоже самое что move_left == True:
        platform.rect.x -= 3

    clock.tick(40)#стандартное 40
    pygame.display.update()

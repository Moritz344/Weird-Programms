import pygame 
import math
import random
import noise

width = 1920
height = 1080
screen= pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption("lines")

cell_size = 10

class Line(object):
    def __init__(self,position,direction,speed=cell_size):
        self.position = pygame.Vector2(position)
        self.speed = speed
        self.time = 0
        self.direction = direction
        
        self.size = 10
        self.snake_len = 30
        self.snake_list =  [] 
        self.snake_head = [self.position.x ,self.position.y ]
        self.snake_list.append(self.snake_head)

    def move(self):
        self.angle = (noise.pnoise1(self.time,repeat=1024) + 1) * math.pi
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        
        if self.direction == "RIGHT":
            self.position.x += self.dx
        else:
            self.position.x -= self.dx 
        if self.direction == "UP":
            self.position.y -= self.dy
        else:
            self.position.y += self.dy 
        
        self.time += 0.01
    
    def collision(self):
       if self.position.x >= width - self.size:
               self.position.x = self.size
               self.dx *= -1
       elif self.position.x <= 0 + self.size:
               self.position.x = width - self.size
               self.dx *= -1
  
       if self.position.y >= height - self.size:
               self.position.y = self.size
               self.dy *= -1
       elif self.position.y <= self.size:
           self.position.y = height - self.size
           self.dy *= -1
  
  

    def draw_line(self):
        for snake in self.snake_list:
            pygame.draw.rect(screen,"white",(snake[0]  ,snake[1],self.size,self.size))
        self.snake_list.append((self.position.x,self.position.y  ))

        if len(self.snake_list ) > self.snake_len :
            del self.snake_list[0]

    def update(self):

        self.draw_line()
        self.move()
        self.collision()

line = [Line((random.randint(0,width),random.randint(0,height)),random.choice(["LEFT","RIGHT","UP","DOWN"]),4) for _ in range(10)]

def spawn_line(group):
    for line in group:
        line.update()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            run = False

    screen.fill("black")

    spawn_line(line)

    clock.tick(60)
    pygame.display.update()
pygame.quit()

import pygame, sys, random
from pygame.math import Vector2

pygame.init()

BG_color = (173,204,96)
SNAKE_COLOR = (43,51,24)

cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = self.generate_random_pos()
    def draw(self):
        Food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(Food_surface, Food_rect)
        
    def generate_random_pos(self):
        x = random.randint(0, number_of_cells -1)
        y = random.randint(0, number_of_cells -1)
        position = Vector2(x, y)
        return position

class Snake:
    def __init__(self):
        self.body =  [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1,0)
        self.add_segment = False
    
    def draw(self): 
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, SNAKE_COLOR, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
         else
        self.body.pop()
        
              
              
screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

pygame.display.set_caption("retro snake")

clock = pygame.time.Clock()

food = Food()
snake = Snake()
game = game()

Food_surface = pygame.image.load("graphics/food.png")

SNAKE_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SNAKE_UPDATE,150)


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SNAKE_UPDATE:
            game.update()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Vector2(0,1):
             snake.direction = Vector2(0, -1)
            if event.key == pygame.K_LEFT:
             snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT :
             snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
             snake.direction = Vector2(0, 1)
            
            
    
            
    
    screen.fill(BG_color)

    snake.draw() 
    
    
    pygame.display.update()
    clock.tick(60)
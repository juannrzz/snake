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
    
    def draw(self): 
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, SNAKE_COLOR, segment_rect, 0, 7)

screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

pygame.display.set_caption("retro snake")

clock = pygame.time.Clock()

food = Food()
snake = Snake()
Food_surface = pygame.image.load("graphics/food.png")


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    screen.fill(BG_color)
    food.draw()
    snake.draw() 
    
    
    pygame.display.update()
    clock.tick(60)
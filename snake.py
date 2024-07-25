import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
FPS = 15
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = (0, -CELL_SIZE)
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % WIDTH, (head_y + dir_y) % HEIGHT)

        if self.grow:
            self.positions = [new_head] + self.positions
            self.grow = False
        else:
            self.positions = [new_head] + self.positions[:-1]

    def change_direction(self, direction):
        opposite_direction = (-self.direction[0], -self.direction[1])
        if direction != opposite_direction:
            self.direction = direction

    def grow_snake(self):
        self.grow = True

    def check_collision(self):
        head = self.positions[0]
        if head in self.positions[1:]:
            return True
        return False

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, RED, (*pos, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def spawn(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, (*self.position, CELL_SIZE, CELL_SIZE))

snake = Snake()
food = Food()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))

            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))

            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))

            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))

    snake.move()

    if snake.positions[0] == food.position:
        snake.grow_snake()
        food.spawn()

    if snake.check_collision():
        running = False

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()




















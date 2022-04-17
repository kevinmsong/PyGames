import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 7, HEIGHT / 2)
    
    def update(self):
        pass
    
class ObstacleTop(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH, HEIGHT / 5)
    
    def update(self):
        self.rect.x -= 7
        
        if self.rect.right <= 0:
            self.rect.x = WIDTH
            
class ObstacleMid(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (2 * WIDTH, HEIGHT / 3)
    
    def update(self):
        self.rect.x -= 5
        
        if self.rect.right <= 0:
            self.rect.x = WIDTH
            
class ObstacleBot(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (1.5 * WIDTH, HEIGHT / 2)
    
    def update(self):
        self.rect.x -= 6
        
        if self.rect.right <= 0:
            self.rect.x = WIDTH
            
class Background(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((360, 70))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 30)
        
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

player = Player()
background = Background()
obstacle_top = ObstacleTop()
obstacle_mid = ObstacleMid()
obstacle_bot = ObstacleBot()

all_sprites.add(player)
all_sprites.add(background)
all_sprites.add(obstacle_top)
all_sprites.add(obstacle_mid)
all_sprites.add(obstacle_bot)


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    
    # Process input (events)
    for event in pg.event.get():        
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Update
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_UP]:
        player.rect.y -= 10
    else:
        if player.rect.y < 350:
            player.rect.y += 10

    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
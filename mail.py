import pygame 

pygame.init()
back = (0,0,0)
mw = pygame.display.set_mode((600,600))
mw.fill(back)

class GameSprite:
    pass

clock = pygame.time.Clock()
game = True
while game:
    for e in pygame.event.get():
        if e.type == QUIT:
            game = False

    pygame.display.update()
    clock.tick(60)

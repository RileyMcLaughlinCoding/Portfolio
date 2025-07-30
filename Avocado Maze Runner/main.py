import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


import pygame
from sys import exit

# screen
pygame.init()
font = pygame.font.SysFont(None, 100)
game_active = True
game_result = ""
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Avocado Maze Runner')
clock = pygame.time.Clock()
white= (255,255,255)
screen.fill(white)

#walls
walls = [
#barriers
pygame.Rect(100,400,15,200),
pygame.Rect(200,100,15,200),
pygame.Rect(400,200,15,200),
pygame.Rect(500,500,15,200),
pygame.Rect(600,500,15,200),
pygame.Rect(1000,100,15,200),
pygame.Rect(1000,500,15,200),
pygame.Rect(1100,300,15,200),
pygame.Rect(200,500,200,15),
pygame.Rect(600,100,200,15),
pygame.Rect(600,300,200,15),
pygame.Rect(800,500,200,15),
pygame.Rect(800,685,200,15),
#border
pygame.Rect(0,-5,1200,15),
pygame.Rect(0,790,1200,15),
pygame.Rect(-5,0,15,800),
pygame.Rect(1190,0,15,800),
]

#start
start = pygame.Rect(0,0,100,100)
red = (255,0,0)
pygame.draw.rect(screen, red, start)

#end
end = pygame.Rect(1100,700,100,100)
green = (0,255,0)
pygame.draw.rect(screen, green, end)

#avocado
avo_surf = pygame.image.load('avocado.png').convert_alpha()
avo_surf = pygame.transform.scale(avo_surf, (75,75))
avo_rect = avo_surf.get_rect(midbottom=(50, 85))

# game state
game_active = True
end_message = ""

def show_end_screen(message):
    screen.fill((0, 0, 0))
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (300, 300))

    subfont = pygame.font.SysFont(None, 36)
    subtext = subfont.render("Press R to restart", True, (200, 200, 200))
    screen.blit(subtext, (420, 380))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not game_active and event.type == pygame.KEYDOWN:
            # Reset the game
            avo_rect.topleft = (50, 25)
            game_result = ""
            game_active = True

    if game_active:
        screen.fill(white)

        pygame.draw.rect(screen, red, start)
        pygame.draw.rect(screen, green, end)
        screen.blit(avo_surf, avo_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            avo_rect.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            avo_rect.x += 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            avo_rect.y += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            avo_rect.y -= 5

        for wall in walls:
            pygame.draw.rect(screen, (255, 0, 0), wall)
            if avo_rect.colliderect(wall):
                game_result = "lose"
                game_active = False

        if avo_rect.colliderect(end):
            game_result = "win"
            game_active = False

    else:
        screen.fill((0, 0, 0))
        if game_result == "lose":
            text = font.render("YOU SUCK", True, (255, 0, 0))
        else:
            text = font.render("YOU DID IT!", True, (0, 255, 0))
        screen.blit(text, text.get_rect(center=(600, 400)))

    pygame.display.update()
    clock.tick(60)


    pygame.display.update()
    clock.tick(60)

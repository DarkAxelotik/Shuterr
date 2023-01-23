import pygame
import os
pygame.init()

def file_path(file_name):
    folder_path = os.path.abspath(__file__+"/..")
    path = os.path.join(folder_path, file_name)
    return path


WIN_WIDTH, WIN_HEIGHT = 700, 500
FPS = 120


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("shuter")
clock = pygame.time.Clock()


play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


            clock.tick(FPS)
    pygame.display.update()
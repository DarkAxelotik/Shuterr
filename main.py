import pygame
import os
pygame.init()

def file_path(file_name):
    folder_path = os.path.abspath(__file__+"/..")
    path = os.path.join(folder_path, file_name)
    return path


WIN_WIDTH, WIN_HEIGHT = 700, 500
FPS = 120


img_background = pygame.image.load(file_path("fon.jpg"))
img_background = pygame.transform.scale(img_background, (WIN_WIDTH, WIN_HEIGHT))

pygame.mixer.music.load(file_path("FNAF_Security_Breach_OST：_＂Fazer_Blast_Jam.wav"))
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("shuter")
clock = pygame.time.Clock()


play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if play == True:
        window.blit(img_background,(0, 0))


    clock.tick(FPS)
    pygame.display.update()
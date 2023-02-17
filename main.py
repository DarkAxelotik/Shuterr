import pygame
import os
from random import randint
pygame.init()

def file_path(file_name):
    folder_path = os.path.abspath(__file__+"/..")
    path = os.path.join(folder_path, file_name)
    return path


WIN_WIDTH, WIN_HEIGHT = 1000, 800
FPS = 120
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

img_background = pygame.image.load(file_path("fon.jpg"))
img_background = pygame.transform.scale(img_background, (WIN_WIDTH, WIN_HEIGHT))

pygame.mixer.music.load(file_path("FNAF_Security_Breach_OST：_＂Fazer_Blast_Jam.wav"))
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)


music_lose = pygame.mixer.Sound(file_path("Music_default_dire_lose.mp3.wav"))
music_win = pygame.mixer.Sound(file_path("Music_default_dire_win.mp3.wav"))

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("shuter")
clock = pygame.time.Clock()


class GameSprite(pygame.sprite.Sprite):
    def __init__ (self, x, y, width, height, img, speed):
        super().__init__()
        self.image = pygame.image.load(file_path(img))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__(x, y, width, height, img, speed)
     
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, 120, 100, file_path("ctrelat.png"), 5) 
        bullets.add(bullet) 
class Bullet(GameSprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__(x, y, width, height, img, speed)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()



class Enemy(GameSprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__(x, y, width, height, img, speed)

    def update(self):
        global score_lose
        self.rect.y += self.speed
        if self.rect.y > WIN_HEIGHT:
            self.rect.x = randint(0,WIN_WIDTH-70)
            score_lose += 1
            self.rect.y = 0

enemys =  pygame.sprite.Group()
for  i in range(5):
    enemy = Enemy(randint(0, WIN_WIDTH - 220), 0, 220, 200, file_path("vrag.png"), randint(1, 7))
    enemys.add(enemy) 


bullets = pygame.sprite.Group()


player = Player(400, 500, 320, 300, file_path("arc_warden.png"), 5)

score_lose = 0 
score_destroy = 0 


font = pygame.font.SysFont("arial", 30, 0, 1)
txt_lose = font.render("skip"+ str(score_lose), True,WHITE)
txt_destroy = font.render("destroy"+ str(score_destroy), True,WHITE)



play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                player.fire()


    if play == True:
        window.blit(img_background,(0, 0))
        txt_lose = font.render("skip"+ str(score_lose), True,WHITE)
        txt_destroy = font.render("destroy"+ str(score_destroy), True,WHITE)

        window.blit(txt_lose, (50,50))
        window.blit(txt_destroy, (50,80))


        player.reset()
        player.update()

        enemys.draw(window)
        enemys.update()

        bullets.draw(window)
        bullets.update()


        enemysandbullet = pygame.sprite.groupcollide(enemys, bullets, False, True)
        if enemysandbullet:
            for enemy  in enemysandbullet:
                score_destroy += 1
                enemy.rect.x = randint(0, WIN_WIDTH -70)
                enemy.rect.y = 0
        if score_lose >= 5 or pygame.sprite.spritecollide(player, enemys, False):
            play = False
            font2 = pygame.font.SysFont("arial", 50, 1)
            txt_gameover = font2.render("LOOOOSE", True, RED)
            window.blit(txt_gameover, (350, 300))
            pygame.mixer.music.stop()
            music_lose.play()

        elif score_destroy >= 1:
            play = False
            font3 = pygame.font.SysFont("arial", 50, 1)
            txt_gameover = font3.render("WIIN", True, GREEN)
            window.blit(txt_gameover, (350, 300))
            pygame.mixer.music.stop()
            music_win.play()

    clock.tick(FPS)
    pygame.display.update()
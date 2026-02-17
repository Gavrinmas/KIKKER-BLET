#https://soundbank.one/tag/ogg/
from pygame import *
from time import time as timer
from random import *
mixer.init()
w = 700
h = 500
font.init()
mixer.music.load('cosmos.mp3')
mixer.music.set_volume(0.3)
mixer.music.play()

clock = time.Clock()

window = display.set_mode((w, h))

display.set_caption('Galaxy')

back = transform.scale(image.load('galaxy.jpg'), (w, h))

game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def fire(self):
        b = Bullet('bullet.png', self.rect.centerx,  self.rect.top, 15, 15, 20)
        bullets.add(b)






lose = 0       
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lose
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(80, 600)
            lose += 1
            ser.play()

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


win_m = 0
live = 3
bullets = sprite.Group()
num_fire = 0
rel_time = False

space = mixer.Sound('fire.ogg')
ser = mixer.Sound('er.mp3')
monsters = sprite.Group()
for i in range(5):
    e = Enemy('ufo.png', randint(80, 600), 0, randint(1, 2), 80, 50)
    monsters.add(e)
aster = sprite.Group()
for i in range(3):
    a = Enemy('asteroid.png', randint(80, 600), 0, randint(1, 2), 80, 50)
    aster.add(a)


p = Player('rocket.png', 350, 400, 10, 80, 100)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == MOUSEBUTTONDOWN and i.button == 1:
            if num_fire < 8 and rel_time == False:
                num_fire += 1
                p.fire()
                space.play()
            if num_fire >= 8 and rel_time == False:
                rel_time = True
                start = timer()
    


     
    if finish != True:
        window.blit(back, (0, 0))
        text_lose = font.SysFont('Arial', 36).render('Пропущено: ' + str(lose), True, (255, 255, 255))
        text_win = font.SysFont('Arial', 36).render('Счет: ' + str(win_m), True, (255, 255, 255))
        p.reset()
        p.update()
        monsters.update()
        monsters.draw(window)
        aster.update()
        aster.draw(window)
        bullets.update()
        bullets.draw(window)
        window.blit(text_lose, (10, 70))
        window.blit(text_win, (10, 30))
        sprite_list = sprite.groupcollide(monsters, bullets, True, True)
        for a in sprite_list:
            win_m += 1
            e = Enemy('ufo.png', randint(80, 600), 0, randint(1, 4), 80, 50)
            monsters.add(e)
        if win_m >= 11:
            text_winner = font.SysFont('Arial', 100).render('ТЫ ВЫИГРАЛ ' , True, (0, 255, 0))
            finish = True
            window.blit(text_winner, (100, 300))
        if lose >= 4 or sprite.spritecollide(p, monsters, False) or sprite.spritecollide(p, aster, False):
            text_losser = font.SysFont('Arial', 100).render('ТЫ ПРОИГРАЛ ' , True, (255, 0, 0))
            finish = True
            window.blit(text_losser, (100, 300))
        if rel_time == True:
            end = timer()
            if end - start <= 3:
                text_reload = font.SysFont('Arial', 20).render('Стой, КУДА, жди, идет перезарядка! ' , True, (0, 255, 0))
                window.blit(text_reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False
    display.update()
    clock.tick(60)
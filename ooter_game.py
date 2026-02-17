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





while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
     
    
    if finish != True:
        window.blit(back, (0, 0))

    display.update()
    clock.tick(60)

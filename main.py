from pygame import *
from random import randint

win = display.set_mode((888,555))
display.set_caption('zxctir')
lost = 0
mixer.init()
mixer.music.load('ddd.mp3')
mixer.music.play()

font.init()
font1 = font.Font(None, 33)
won = font1.render('WIN',True,(0,4,222))
lose = font1.render('LOSE',True,(0,4,222))
font2 = font.Font(None, 22)


game = True
class GameSprite(sprite.Sprite):
    def __init__(self , p_img , p_x , p_y ,p_spe, p_s_x , p_s_y ):
        super().__init__()
        self.image = transform.scale(image.load(p_img) , (p_s_x , p_s_y ))
        self.speed = p_spe
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        win.blit(self.image,(self.rect.x , self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0 :
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 800 :
            self.rect.x += self.speed

def fire(self):
    pass


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 888:
            self.rect.y = 0
            self.rect.x = randint(50,888-50)
            lost = lost + 1
            print(lost)
        

bg = GameSprite('orig.jpg', 0, 0, 0, 1000, 900)
play = Player('Ананас.png', 300, 444, 5, 50 , 50)
eney = GameSprite('fg.png', 600, 1, 5, 50 , 50) #поменяить
bullet = GameSprite('bullet.png', 300, 400, 5, 33 , 33) #поменяить
Enemys = sprite.Group()
for i in range(1,10):
    enemy = Enemy('fg.png' , randint(50,888-50),10,6,50,50)
    Enemys.add(enemy)

clock = time.Clock()
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    text_score = font2.render('Счет: '+str(0), True , (0,40,2))
    txt_lose = font2.render('poter: '+str(lost), True , (111,40,2))

    bg.reset()
    win.blit(text_score, (10,10))
    win.blit(txt_lose, (10,33))
    play.update()
    play.reset()
    bullet.update()
    bullet.reset()
    Enemys.draw(win)
    Enemys.update()
  
    
    
    
    
    display.update()
    clock.tick(60)
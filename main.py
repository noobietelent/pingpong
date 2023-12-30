from pygame import *

'''Необхідні класи'''


#клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))  # разом 55,55 - параметри
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self,):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self, ):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 60
raketka_1 = Player("racket.png", 30, 200, 4, 50, 150)
raketka_2 = Player("racket.png", 520, 200, 4, 50, 150)
myachik = GameSprite("ball.png", 200, 200, 4, 50, 50)
font.init()
font = font.Font(None, 35)
lose_1 = font.render("p_1 lose", True,(180, 0, 0))
lose_2 = font.render("p_2 lose", True,(180, 0, 0))
speed_x = 3
speed_y = 3
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(back)
        raketka_1.update_l()
        raketka_2.update_r()
        myachik.rect.x += speed_x
        myachik.rect.y += speed_y
        if sprite.collide_rect(raketka_1, myachik) or sprite.collide_rect(raketka_2, myachik):
            speed_x *= -1
            speed_y *= 1
        if myachik.rect.y > win_height - 50 or myachik.rect.y < 0:
            speed_y *= -1
        if myachik.rect.x < 0:
            finish = True
            window.blit(lose_1, (200, 200),)
            game_over = True
        if myachik.rect.x > win_width:
            finish = True
            window.blit(lose_2, (200, 200),)
            game_over = True
        raketka_1.reset()
        raketka_2.reset()
        myachik.reset()

    display.update()
    clock.tick(FPS)
from pygame import *
from random import randint

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Jumper')
game = True

FPS = 60
clock = time.Clock()

fon = transform.scale(image.load('fon_1.jpg'), (700, 500))

fon_game_over = transform.scale(image.load('fon_2.jpg'), (700, 500))

amount_proiden = 0


mixer.init()
mixer.music.load('Breathe.mp3')
mixer.music.play()
otbev = mixer.Sound('otbev.ogg')



font.init()
font1 = font.SysFont('Arial', 30)
score_proiden = font1.render(f'Ваш счёт: '+ str(amount_proiden), True, (100, 100, 100))
font2 = font.SysFont('Arial', 50)
game_over = font2.render('Игра окончена', True, (200, 100, 100))
game_over_score = font2.render('Ваш счёт:' + str(amount_proiden), True, (150, 100, 100))

amount_jump = 0
jump = False

class Platform (sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, rect_x, rect_y, speed):
        super().__init__()
        self.color_1 = color_1
        self.color_3 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
        

    def update(self):
        self.rect.y += 1
        if self.rect.y >= 490:
            self.rect.y = randint(0, 100)
            self.rect.x = randint(10, 690)
    #    window.blit(self.image, (self.rect.x, self.rect.y))
    def fall(self):
        self.rect.y += self.speed

    # def reset(self):
    #     self.rect.y -= 5



    
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed_x, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    
    def jump(self):
        global amount_jump, jump
        if amount_jump <= 100:
            amount_jump += 1
            self.rect.y -= 2
        else:
            jump = False
            amount_jump = 0
        


player = GameSprite('ball_stal.png', 50, 400, 50, 30, 3, 3)



platforms = sprite.Group()
#fall_platforms = sprite.Group()

platform = Platform(100, 80, 0, 100, 10, 50, 450, 0)
platforms.add(platform)
for i in range(5):
    platform = Platform(100, 80, 0, 100, 10, randint(0,700), randint(150,450), 0)
    platforms.add(platform)
# for i in range(2):
    fall_platform = Platform(100, 80, 0, 100, 10, randint(0,700), 0, 2)
#     fall_platforms.add(fall_platform)








finish = False


while game:
    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:

        window.blit(fon, (0, 0))
        platforms.draw(window)
        window.blit(fall_platform.image, (fall_platform.rect.x, fall_platform.rect.y))
        fall_platform.fall()
        #platforms.update()
        player.reset()
        score_proiden = font1.render(f'Вы уничтожили: '+ str(amount_proiden), True, (100, 100, 100))

        window.blit(score_proiden, (0, 30))
    
        # if keys[K_SPACE]:
        #     jump = True
        #     player.jump()
        
        if keys[K_LEFT]:
            player.rect.x -= player.speed_x
        
        if keys[K_RIGHT]:
            player.rect.x += player.speed_x
        
        if jump == False:
            player.rect.y += 2
        else:
            player.jump()
        
        
        if (sprite.spritecollide(player, platforms, False) or player.colliderect(fall_platform.rect) )and jump == False:
            otbev.play()
            jump = True
        
        if player.rect.x > 700:
            player.rect.x = 0

        if player.rect.x < 0 :
            player.rect.x = 700


        if player.rect.y < 150:
            amount_proiden += 1
            platforms.update()
            player.rect.y += 2
        
        if player.rect.y > 475:
            game_over = font2.render('Игра окончена', True, (150, 100, 100))
            game_over_score = font2.render('Ваш счёт:' + str(amount_proiden), True, (200, 100, 100))
            finish = True

        if fall_platform.rect.y >= 490:
            fall_platform.rect.y = 0
            fall_platform.rect.x = randint(10, 690)
    else:
        window.blit(fon_game_over, (0, 0))
        window.blit(game_over, (0, 250))
        window.blit(game_over_score, (0, 350))

            





    clock.tick(FPS)
    display.update()
















from pygame import *
width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Ping pong')

FPS = 60
clock = time.Clock()

game = True

fon = transform.scale(image.load('fon.jpg'), (700, 500))

















class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Platforma1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 635:
            self.rect.y += self.speed










#platforma1 = Platforma1('')



finish = False

while game == True:

    keys = key.get_pressed()
    


    for e in event.get():
        if e.type == QUIT:
            game = False


    

    if finish != True:
        window.blit(fon, (0, 0))




    
    
    clock.tick(FPS)
    display.update()

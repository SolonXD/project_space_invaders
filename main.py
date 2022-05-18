import pygame
import os
import random
import time
pygame.init()
width, height = 500, 800
win = pygame.display.set_mode((width, height))
    

def load_image(name, colorkey=None):
    fullname = os.path.join('data\images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
    image = pygame.image.load(fullname)
    return image


player_lose = False
alien_lose = False

background = pygame.sprite.Sprite()
background.image = load_image('space_background.jpg')
background.rect = background.image.get_rect()
background.rect.x = 0
background.rect.y = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, x, y, picture_name):
        super(Enemy, self).__init__()
        self.image = load_image(picture_name)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.shooter = Shooter('enemy')
        self.add(group)


class Enemy1(Enemy):
    def update(self):
        if pygame.sprite.spritecollideany(self, bullets_group):
            self.kill()
            sprites = bullets_group.sprites()
            bullet = sprites[0]
            pygame.sprite.Group.remove(bullets_group, bullet)
        else:
            win.blit(self.image, (self.rect.x, self.rect.y))


class Enemy2(Enemy):
    def update(self):
        if pygame.sprite.spritecollideany(self, bullets_group):
            self.kill()
            sprites = bullets_group.sprites()
            bullet = sprites[0]
            pygame.sprite.Group.remove(bullets_group, bullet)
        else:
            win.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self):
        if random.randint(1, 251) == 1:
            Bullet(bullets_group_enemy, self.rect.x + 20, self.rect.y + 20, 3)


class Player(pygame.sprite.Sprite):
    def __init__(self, life=True):
        self.pressed = False
        self.team = 'ally'
        self.image = load_image('playermodel.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 700
        self.life = life

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x <= 450:
            self.rect.x += 3
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= 3

    def update(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.pressed:
            Shooter.shoot(self, self.rect.x + 20, self.rect.y - 20)
            self.pressed = True
        if not keys[pygame.K_SPACE]:
            self.pressed = False
        if pygame.sprite.spritecollideany(self, bullets_group_enemy):
            self.life = False


class Shooter:
    def __init__(self, team='ally'):
        self.team = team
        self.x = 0

    def shoot(self, x, y):
        self.x = x
        self.y = y
        if self.team == 'ally':
            Bullet(bullets_group, self.x, self.y, -3)
        else:
            Bullet(bullets_group_enemy, self.x, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, x_coords=225, y_coords=700, y=0):
        super(Bullet, self).__init__()
        self.add(group)
        self.x_coords = x_coords
        self.y = y
        self.y_coords = y_coords
        self.rect = pygame.rect.Rect(self.x_coords, self.y_coords, 10, 10)

    def update(self):
        if (self.rect.y > 0) and (self.rect.y < 800):
            self.rect = self.rect.move(0, self.y)
        else:
            self.kill()
        pygame.draw.rect(win, (255, 255, 255), self.rect)


def end_screen():
    if alien_lose is True:
        intro_text = ["You Win",
                      "Good Game!"]
        winner = 'Red'
    elif player_lose is True:
        intro_text = ["Aliens Wins",
                      "Well Played!"]
        winner = 'Green'
    fon = load_image('space_background.jpg')
    win.blit(fon, (0, 0))
    font = pygame.font.Font(None, 60)
    text_coord = 200
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color(winner))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 120
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)


run = True
targets_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
bullets_group_enemy = pygame.sprite.Group()
a = Enemy2(targets_group, 20, 200, 'enemy2.png')
b = Enemy2(targets_group, 120, 200, 'enemy2.png')
c = Enemy2(targets_group, 220, 200, 'enemy2.png')
d = Enemy2(targets_group, 320, 200, 'enemy2.png')
e = Enemy2(targets_group, 420, 200, 'enemy2.png')
f = Enemy2(targets_group, 20, 100, 'enemy2.png')
array_enemy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
array_enemy[0] = Enemy2(targets_group, 20, 200, 'enemy2.png')
array_enemy[1] = Enemy2(targets_group, 120, 200, 'enemy2.png')
array_enemy[2] = Enemy2(targets_group, 220, 200, 'enemy2.png')
array_enemy[3] = Enemy2(targets_group, 320, 200, 'enemy2.png')
array_enemy[4] = Enemy2(targets_group, 420, 200, 'enemy2.png')
array_enemy[5] = Enemy2(targets_group, 20, 100, 'enemy2.png')
array_enemy[6] = Enemy2(targets_group, 120, 100, 'enemy2.png')
array_enemy[7] = Enemy2(targets_group, 220, 100, 'enemy2.png')
array_enemy[8] = Enemy2(targets_group, 320, 100, 'enemy2.png')
array_enemy[9] = Enemy2(targets_group, 420, 100, 'enemy2.png')
array_enemy[10] = Enemy2(targets_group, 70, 50, 'enemy2.png')
array_enemy[11] = Enemy2(targets_group, 170, 50, 'enemy2.png')
array_enemy[12] = Enemy2(targets_group, 270, 50, 'enemy2.png')
array_enemy[13] = Enemy2(targets_group, 370, 50, 'enemy2.png')
array_enemy[14] = Enemy2(targets_group, 70, 150, 'enemy2.png')
array_enemy[15] = Enemy2(targets_group, 170, 150, 'enemy2.png')
array_enemy[16] = Enemy2(targets_group, 270, 150, 'enemy2.png')
array_enemy[17] = Enemy2(targets_group, 370, 150, 'enemy2.png')


def lvl1():
    Enemy1(targets_group, 20, 250, 'enemy1.png')
    Enemy1(targets_group, 120, 250, 'enemy1.png')
    Enemy1(targets_group, 220, 250, 'enemy1.png')
    Enemy1(targets_group, 320, 250, 'enemy1.png')
    Enemy1(targets_group, 420, 250, 'enemy1.png')
    Enemy1(targets_group, 20, 150, 'enemy1.png')
    Enemy1(targets_group, 120, 150, 'enemy1.png')
    Enemy1(targets_group, 220, 150, 'enemy1.png')
    Enemy1(targets_group, 320, 150, 'enemy1.png')
    Enemy1(targets_group, 420, 150, 'enemy1.png')


d = 0


def shooting():
    k = 0
    global d
    for i in range(len(array_enemy)):
        if k == len(array_enemy):
            break
        if array_enemy[i] in targets_group:
            array_enemy[i].shoot()
        else:
            k += 1
    if k > 17:
        d += 1


lvl1()
p = Player()
start = pygame.key.get_pressed()


while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    win.blit(background.image, (background.rect.x, background.rect.y))
    targets_group.update()
    p.update()
    p.move()
    bullets_group.update()
    bullets_group_enemy.update()
    shooting()
    if p.life is False:
        player_lose = True
        break
    if d == len(array_enemy):
        alien_lose = True
        break
    pygame.time.Clock().tick(50)
    pygame.display.update()


pygame.sprite.Group.empty(bullets_group)
pygame.sprite.Group.empty(bullets_group_enemy)
pygame.sprite.Group.empty(targets_group)
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    end_screen()
    pygame.time.Clock().tick(50)
    pygame.display.update()
pygame.quit()

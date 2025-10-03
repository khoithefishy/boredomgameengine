import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True
move_direction = pg.math.Vector2()

# Classes:

class Square:
    def __init__(self, x, y, color, size, speed):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        self.size = 25
    def draw(self, screen):
        pg.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])
square = Square(418, 461, "red", 10, 5)

class Bullet:
    def __init__(self, x, y, color, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
    def draw(self, screen):
        pg.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])
bullet = Bullet(square.x, square.y, "yellow", 10, 5)
bullets = []

while running:
    key = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if len(bullets) < 10:
                    new_bullet = Bullet(square.x, square.y, "yellow", 10, 5)
                    bullets.append(new_bullet)
    if key[pg.K_w]:
        square.y -= square.speed
    if key[pg.K_s]:
        square.y += square.speed
    if key[pg.K_a]:
        square.x -= square.speed
    if key[pg.K_d]:
        square.x += square.speed

    for bullet in bullets:
        bullet.y -= bullet.speed
        if bullet.y < 0:
            bullets.remove(bullet)

    if move_direction.length() != 0:
        move_direction = move_direction.normalize() * square.speed
    square.x += move_direction.x
    square.y += move_direction.y

    screen.fill("black")
    square.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)
    pg.display.flip()
    clock.tick(60)
pg.quit()
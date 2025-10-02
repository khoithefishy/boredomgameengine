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
    def draw(self, screen):
        pg.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])
square = Square(418, 461, "red", 10, 5)

while running:
    key = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if key[pg.K_w]:
        square.y -= square.speed
    if key[pg.K_s]:
        square.y += square.speed
    if key[pg.K_a]:
        square.x -= square.speed
    if key[pg.K_d]:
        square.x += square.speed

    if move_direction.length() != 0:
        move_direction = move_direction.normalize() * square.speed
    square.x += move_direction.x
    square.y += move_direction.y

    screen.fill("black")
    square.draw(screen)
    pg.display.flip()
    clock.tick(60)
pg.quit()
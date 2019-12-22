import pygame
from random import randrange as rnd

clalist = []
sizex, sizey = 400, 300


class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.xd = 0
        self.yd = 1
        self.color = color

    def dl(self):
        self.x += self.xd
        self.y += self.yd
        if (self.x <= 0) or (self.x >= sizex):
            self.xd *= -1
        if (self.y <= 0):
            self.yd *= -1
        if (self.y >= sizey - 10):
            self.yd = 0

    def me(self):
        return (self.x, self.y)

    def ce(self):
        return self.color


pygame.init()
screen = pygame.display.set_mode([sizex, sizey])
fps = 100
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            clalist.append(Ball(event.pos[0], event.pos[1], (rnd(255), rnd(255), rnd(255))))
    for v in clalist:
        pygame.draw.circle(screen, v.ce(), v.me(), 5)
        v.dl()
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()

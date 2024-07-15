import pygame
from pad import Pad
from ball import Ball

class Game():
    def __init__(self):
        self.width = 1200
        self.height = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption('Pong')
        self.left_pad = Pad(self, 1)
        self.right_pad = Pad(self, 0)
        self.ball = Ball(self)

    def quit(self):
        pygame.quit()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.right_pad.move(-1)
        if keys[pygame.K_DOWN]:
            self.right_pad.move(1)
        if keys[pygame.K_w]:
            self.left_pad.move(-1)
        if keys[pygame.K_s]:
            self.left_pad.move(1)

        self.screen.fill((235,222,220))
        self.left_pad.draw(20)
        self.right_pad.draw(20)
        self.ball.draw()
        pygame.display.flip()

        self.clock.tick(60)
    
play = Game()

while(play.running):
    play.run()

play.quit()
import pygame

class Ball():
    def __init__(self, screen):
        self.radius = 10
        self.screen = screen
        self.x = screen.width/2 - self.radius
        self.y = screen.height/2 - self.radius
        
        
    def draw(self):
        self.ball = pygame.draw.circle(self.screen.screen, (223,157,192), (self.x + self.radius, self.y + self.radius), self.radius)
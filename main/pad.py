import pygame

class Pad():
    def __init__(self, screen, position:int):
        self.width = 20
        self.height = 100
        self.speed = 5
        if position == 0:
            self.x = screen.width - self.width * 2
        else:
            self.x = self.width
        self.y = screen.height/2 - self.height/2
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, y:int):
        self.rect.topleft = (self.x, self.y)
        pygame.draw.rect(self.screen.screen, (223,157,192), self.rect)

    def move(self, direction:int):
        if direction < 0: # Ir para cima
            if self.y <= 0:
                self.y = 0
            else:
                self.y -= self.speed
        if direction > 0: # Ir para baixo
            if self.y + self.height >= self.screen.height:
                self.y = self.screen.height - self.height
            else:
                self.y += self.speed
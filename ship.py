import pygame   # para o funcionamento da nave, é necessario pygame

class Ship():
    def __init__(self, screen):     # espaco que a nave ocupara
        self.screen = screen        # salvando como uma variavel screen

        self.image = pygame.image.load('images/ship.bmp')   # load carrega a imagem da nave, e armazena como self.image
        self.rect = self.image.get_rect()   
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blime(self):
        self.screen.blit(self.image, self.rect)

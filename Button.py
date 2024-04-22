import pygame
from utils.Scaling import get_image

class Button:
    def __init__(self, position : list[float,float,float,float], main):
        self.main = main
        self.rect = pygame.Rect(position)

    def handle_click(self, button):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.on_click(button)
            return True
        return False
    def on_render(self):
        pass
    def on_click(self, button):
        pass

class BaseButton(Button):
    def __init__(self, id : int, imageUrl, position : list[float,float,float], main):
        self.id = id
        self.imageUrl = imageUrl
        self.image = get_image(pygame.image.load(imageUrl), position[2])

        self.main = main

        self.rect = self.image.get_rect()
        self.rect.topleft = position[0], position[1]
    def on_render(self):
        self.main.display.blit(self.image, self.rect)
    def on_click(self, button):
        if self.id == 3:
            self.main.TILED = not self.main.TILED
            self.main.alerts.create_alert("assets/alerts/check-mark.png")
        if self.id == 0:
            self.main.tile_display.open = not self.main.tile_display.open
            self.main.alerts.create_alert("assets/alerts/check-mark.png")

class TileButton(Button):
    def __init__(self, imageUrl, position : list[float,float,float], main):
        self.id = id
        self.imageUrl = imageUrl
        self.image = get_image(pygame.image.load(imageUrl), position[2])

        self.main = main

        self.rect = self.image.get_rect()
        self.rect.topleft = position[0], position[1]
    def on_render(self):
        self.main.display.blit(self.image, self.rect)
    def on_click(self, button):
        pass
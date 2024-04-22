import pygame

def get_image(image : pygame.Surface, new_width : float):
    scale = new_width / image.get_width()

    return pygame.transform.scale(image, (new_width, image.get_height()*scale))
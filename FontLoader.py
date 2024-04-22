import pygame,os

FONTS = []

def load_fonts():
    FONTS.clear()
    for f in os.listdir("assets/font"):
        if not f.endswith(".ttf"):
            continue
        FONTS.append((f[0:len(f)-4], pygame.font.Font("assets/font/" + f, 20)))
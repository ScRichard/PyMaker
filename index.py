import pygame
import FontLoader as font
import animation.Animation as Animation
import Button
import Alerts

class App:
    def __init__(self):
        self.SCREEN_SIZE = (800,600)

        self.running = True

        pygame.init()

        self.display = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("PyMaker | Simple map maker")

        self.alerts = Alerts.Alerts(self.display)

        self.tile_display = TileDisplay(self)

        self.TILED = False

        self.movement = [0, 0]

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.clock = pygame.time.Clock()

        self.buttons = [
            Button.BaseButton(0, "assets/buttons/open-list-button.png", [0, self.SCREEN_SIZE[1]/2-20, 20], self),
            Button.BaseButton(1, "assets/buttons/load-button.png", [self.SCREEN_SIZE[0]-35, 5, 30], self),
            Button.BaseButton(2, "assets/buttons/save-button.png", [self.SCREEN_SIZE[0] - 35, 40, 30], self),
            Button.BaseButton(3, "assets/buttons/tile-button.png", [self.SCREEN_SIZE[0] - 35, 75, 30], self)
        ]

        font.load_fonts()
    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.display.fill((0,0,0))

            if self.moving_right:
                self.movement[0] -= 2
            if self.moving_left:
                self.movement[0] += 2
            if self.moving_up:
                self.movement[1] += 2
            if self.moving_down:
                self.movement[1] -= 2

            self.renderTiledBackground()

            self.tile_display.on_render()

            for button in self.buttons:
                if button.id == 0:
                    button.rect.x = self.tile_display.animation.get()*200
                button.on_render()

            self.alerts.on_render()

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.handle_click(event.button):
                    return
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    self.moving_up = 1
                case pygame.K_DOWN:
                    self.moving_down = 1
                case pygame.K_LEFT:
                    self.moving_left = 1
                case pygame.K_RIGHT:
                    self.moving_right = 1
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_UP:
                    self.moving_up = 0
                case pygame.K_DOWN:
                    self.moving_down = 0
                case pygame.K_LEFT:
                    self.moving_left = 0
                case pygame.K_RIGHT:
                    self.moving_right = 0

    def renderTiledBackground(self):
        if not self.TILED:
            return
        for y in range(round(300/40)+2):
            pygame.draw.line(self.display, (100,100,100), (0, self.get_center()[1] - round(self.movement[1] / 40) * 40+40*y), (self.display.get_width(), self.get_center()[1] - round(self.movement[1] / 40) * 40+40*y))
            pygame.draw.line(self.display, (100, 100, 100), (0, self.get_center()[1] - round(self.movement[1] / 40) * 40 - 40 * y),
                             (self.display.get_width(), self.get_center()[1] - round(self.movement[1] / 40) * 40 - 40 * y))
        for x in range(round(400 / 40) + 2):
            pygame.draw.line(self.display, (100, 100, 100),
                             (self.get_center()[0] - round(self.movement[0] / 40) * 40 - 40 * x, 0), (
                             self.get_center()[0] - round(self.movement[0] / 40) * 40 - 40 * x,
                             self.display.get_height()))
            pygame.draw.line(self.display, (100, 100, 100),
                             (self.get_center()[0] - round(self.movement[0] / 40) * 40 + 40 * x, 0),
                             (self.get_center()[0] - round(self.movement[0] / 40) * 40 + 40 * x,
                              self.display.get_height()))
    def get_center(self):
        return self.SCREEN_SIZE[0]/2+self.movement[0],  self.SCREEN_SIZE[1]/2+self.movement[1]


class TileDisplay:
    def __init__(self, app):
        self.app = app

        self.open = False
        self.animation = Animation.Animation(200, animationType=Animation.EaseInOutSine())
        self.animation.reset()

        self.display = pygame.Surface((200, self.app.SCREEN_SIZE[1]))
    def on_render(self):
        self.animation.reversed = not self.open

        self.display.fill((165,66,51))
        pygame.draw.rect(self.display, (122,49,37),self.display.get_rect(), 3)
        self.app.display.blit(self.display, (-200+ self.animation.get() * 200,0))


if __name__ == "__main__":
    app = App()
    app.run()
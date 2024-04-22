
import pygame
from animation.Timer import Timer
import animation.Animation as Animation
from utils.Scaling import get_image

class Alert:
    def __init__(self, display_icon_url, start_position : list[float, float], end_position : list[float, float], display):
        self.background = get_image(pygame.image.load("assets/alerts/alert-box.png"), 150)

        self.icon = get_image(pygame.image.load(display_icon_url), self.background.get_height()-40)
        self.display = display
        self.animation = Animation.Animation(500, Animation.EaseOutCubic())
        self.timer = Timer()
        self.start_position = start_position
        self.diff_position = end_position[0]-start_position[0], end_position[1]-start_position[1]
    def on_render(self):
        if self.animation.is_finished() and not self.animation.reversed:
            if self.timer.has_ellapsed(1000, True):
                self.animation.reversed = True
        self.display.blit(self.background, (self.start_position[0] + self.diff_position[0] * self.animation.get(), self.start_position[1] + self.diff_position[1] * self.animation.get()))
        self.display.blit(self.icon, (self.start_position[0] + self.diff_position[0] * self.animation.get()+20, self.start_position[1] + self.diff_position[1] * self.animation.get()+20))
    def can_be_removed(self):
        if self.animation.is_finished() and self.animation.reversed:
            return True
        return False
class Alerts:
    def __init__(self, display):
        self.alerts = []
        self.display = display
    def on_render(self):
        if len(self.alerts) > 0:
            if self.alerts[0].can_be_removed():
                self.alerts.pop(0)
                return
            self.alerts[0].on_render()
    def create_alert(self, display_icon_url):
        self.alerts.append(Alert(display_icon_url, [self.display.get_width()/2 - 75,-80], [self.display.get_width()/2 - 75,10], self.display))
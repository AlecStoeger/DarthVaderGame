# Alec Stoeger
# CS1400 - MWF 8:30
import pygame
from random import randint

X = 0
Y = 1

class Treasure:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("assets/task5_coin(resized).png")
        self.width = self.image.get_width()  # 50px
        self.height = self.image.get_height()  # 39px
        self.radius = self.width //2

        self.sound_effect = pygame.mixer.Sound("assets/treasure-task5(cut).mp3")

        self.center_pos = [randint(self.radius, screen_width - self.radius),
                           randint(self.radius, screen_height - self.radius)]
        self.draw_pos = [self.center_pos[X] - self.width // 2, self.center_pos[Y] - self.height // 2]

    def play_sound(self, mute):
        if not mute:
            pygame.mixer.Sound.play(self.sound_effect)

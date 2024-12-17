# Alec Stoeger
# CS1400 - MWF 8:30
import pygame


X = 0
Y = 1


class Bomb:
    def __init__(self, move, screen_width, screen_height):
        self.sound_effect = pygame.mixer.Sound("assets/what_qjPCUH2B.mp3")
        self.image = pygame.image.load("assets/task5_bomb(resized).png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width // 2
        self.limit = [screen_width, screen_height]
        self.mvmt = move
        self.center_pos = [screen_width // 2, screen_height // 2]
        self.draw_pos = [self.center_pos[X] - self.width // 2, self.center_pos[Y] - self.height // 2]

    def move(self, mute):
        if self.draw_pos[X] + self.width >= self.limit[X] or self.draw_pos[X] <= 0:
            self.mvmt[X] *= -1
            self.play_sound(mute)
        if self.draw_pos[Y] + self.height >= self.limit[Y] or self.draw_pos[Y] <= 0:
            self.mvmt[Y] *= -1
            self.play_sound(mute)

        self.draw_pos[X] += self.mvmt[X]
        self.draw_pos[Y] += self.mvmt[Y]
        self.center_pos[X] += self.mvmt[X]
        self.center_pos[Y] += self.mvmt[Y]
        return self.draw_pos, self.center_pos

    def play_sound(self, mute):
        if not mute:
            pygame.mixer.Sound.play(self.sound_effect)

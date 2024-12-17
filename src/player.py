# Alec Stoeger
# CS1400 - MWF 8:30
import pygame

X = 0
Y = 1


class Player:
    def __init__(self, move, screen_width, screen_height):
        self.image = pygame.image.load("assets/task5_player(resized).png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width // 2
        self.mvmt = move

        self.center_pos = [screen_width // 2, screen_height - self.radius]
        self.draw_pos = [self.center_pos[X] - self.width // 2, self.center_pos[Y] - self.height // 2]

    def move(self, axis, direction):
        self.draw_pos[axis] += self.mvmt[axis] * direction
        self.center_pos[axis] += self.mvmt[axis] * direction

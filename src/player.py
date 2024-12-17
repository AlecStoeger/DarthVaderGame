import pygame

X = 0
Y = 1


# player probably needs an isTouching() method to clean some code up
class Player:
    def __init__(self, move, screen_width, screen_height):
        self.image = pygame.image.load("assets/task5_player(resized).png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width // 2
        self.mvmt = move

        self.center_pos = [screen_width // 2, screen_height - self.radius]
        self.draw_pos = [
                self.center_pos[X] - self.width // 2,
                self.center_pos[Y] - self.height // 2
                ]

    def move(self, axis, direction):
        self.draw_pos[axis] += self.mvmt[axis] * direction
        self.center_pos[axis] += self.mvmt[axis] * direction

    def is_touching(self, coords, obj_width, obj_height):
        return abs(coords[X] - self.center_pos[X]) <= obj_width // 2 + self.radius and \
            abs(coords[Y] - self.center_pos[Y]) <= obj_height // 2 + self.radius

import pygame
from random import randint
from options import Options
from bomb import Bomb
from player import Player
from treasure import Treasure

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
X = 0
Y = 1
CLOCK_TICK = 30
TITLE = "DVG"
ASSETS_DIR = "assets/"

# Setup pygame stuff and clock for framerate
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Set up game media images, sounds
background = pygame.image.load(ASSETS_DIR + "task5_background.png")
game_won = pygame.mixer.Sound(ASSETS_DIR + "win_screen_task5.mp3")
game_lost = pygame.mixer.Sound(ASSETS_DIR + "game-over-task5(cut).mp3")
pygame.mixer.music.load(ASSETS_DIR + "star-wars-cantina-song(cut).mp3")
pygame.mixer.music.set_volume(1.5)

# Set up game data
options = Options()
bomb_list = [
    Bomb([17, randint(6, 30)], SCREEN_WIDTH, SCREEN_HEIGHT),
    Bomb([-17, randint(6, 30)], SCREEN_WIDTH, SCREEN_HEIGHT)
    ]
player = Player([15, 15], SCREEN_WIDTH, SCREEN_HEIGHT)
treasure_list = [Treasure(SCREEN_WIDTH, SCREEN_HEIGHT) for i in range(10)]

# non pygame variables needed for game loop
game_over = False

# game needs to run in a while loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        # game checks buttons that aren't movement buttons
        # (o for options, m for mute when in options)
        # The game should probably just check if you're in options, and then 
        # run an options script if that's the case.

    if game_over:
        pygame.mixer.music.stop()

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.draw_pos[Y] >= 0:
        player.move(Y, -1)
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.draw_pos[Y] + player.height <= SCREEN_HEIGHT:
        player.move(Y, 1)
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.draw_pos[X] >= 0:
        player.move(X, -1)
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.draw_pos[X] + player.width <= SCREEN_WIDTH:
        player.move(X, 1)

    for i in range(len(bomb_list) - 1):
        bomb_list[i].move(options.mute)

    # change this to some sort of method
    for i in treasure_list:
        # this method call is probably slowing the game down
        if player.is_touching(i.center_pos, i.width, i.height):
            treasure_list.remove(i)
            i.play_sound(options.mute)

    if len(treasure_list) == 0:
        options.play_sound(pygame.mixer.Sound.play, game_won)
        color = "green"
        message = pygame.font.SysFont("timesnewroman", 100).render(
                "Congrats!", True, color)
        game_over = True

    for i in bomb_list:
        # same here
        if player.is_touching(i.center_pos, i.width - 25, i.height - 25):
            options.play_sound(pygame.mixer.Sound.play, game_lost)
            color = "red"
            message = pygame.font.SysFont("timesnewroman", 100).render(
                    "Try Again?", True, color)
            game_over = True

    # Always Display
    screen.fill("black")
    screen.blit(background, (0, 0))

    # maybe make these two into a function since they're not likely to 
    # change any time soon
    # Display game
    if not game_over:
        for i in range(len(treasure_list) - 1):
            screen.blit(treasure_list[i].image, [treasure_list[i].draw_pos[X], treasure_list[i].draw_pos[Y]])
        for i in range(len(bomb_list) - 1):
            screen.blit(bomb_list[i].image, [bomb_list[i].draw_pos[X], bomb_list[i].draw_pos[Y]])
        screen.blit(player.image, [player.draw_pos[X], player.draw_pos[Y]])
    # Display menu
    else:
        if options.options_menu:
            options.show_menu()
        else:
            screen.blit(
                    pygame.font.SysFont("timesnewroman", 100)
                    .render("Game Over", True, color), [100, 100])
            screen.blit(message, [100, 250])
            screen.blit(pygame.font.SysFont("timesnewroman", 60)
                        .render("Press o for options", True, color), [100, 400])

    pygame.display.flip()


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

def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    background = pygame.image.load(ASSETS_DIR + "task5_background.png")
    game_won = pygame.mixer.Sound(ASSETS_DIR + "win_screen_task5.mp3")
    game_lost = pygame.mixer.Sound(ASSETS_DIR + "game-over-task5(cut).mp3")
    pygame.mixer.music.load(ASSETS_DIR + "star-wars-cantina-song(cut).mp3")

    ##########
    # Set up game data
    ##########
    # options
    options = Options()
    bomb_list = []
    bomb_list.append(Bomb([17, randint(6,30)], SCREEN_WIDTH, SCREEN_HEIGHT))
    bomb_list.append(Bomb([-17, randint(6,30)], SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player([15, 15], SCREEN_WIDTH, SCREEN_HEIGHT)

    #treasure_list = []
    for i in range(10):
        treasure_list = [Treasure(SCREEN_WIDTH, SCREEN_HEIGHT) for i in range(10)]
        #treasure_list.append(Treasure(SCREEN_WIDTH, SCREEN_HEIGHT))

    ##########
    # Game Loop
    ##########
    pygame.mixer.music.set_volume(1.5)
    game_over = False
    running = True
    while running:
        ##########
        # Get Input/Events
        ##########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o and game_over:
                    options.options_menu = options.toggle(options.options_menu)
                if event.key == pygame.K_m and game_over and options.options_menu:
                    options.mute = options.toggle(options.mute)
                if event.key == pygame.K_SPACE and game_over:

                    # Do Stuff to Reset Game
                    player.center_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - player.radius]
                    player.draw_pos = [player.center_pos[X] - player.width // 2,
                                       player.center_pos[Y] - player.height // 2]

                    for i in bomb_list:
                        i.center_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
                        i.draw_pos = [i.center_pos[X] - i.width // 2,
                                      i.center_pos[Y] - i.height // 2]
                        i.mvmt[Y] = randint(6, 30)

                    treasure_list = []
                    for i in range(10):
                        treasure_list.append(Treasure(SCREEN_WIDTH, SCREEN_HEIGHT))
                    if not options.mute:
                        pygame.mixer.stop()
                        pygame.mixer.music.play(-1)

                    options.options_menu = False
                    game_over = False

        ##########
        # Update state of components/data
        ##########
        if not game_over:
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.draw_pos[Y] >= 0:
                player.move(Y, -1)
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.draw_pos[Y] + player.height <= SCREEN_HEIGHT:
                player.move(Y, 1)
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.draw_pos[X] >= 0:
                player.move(X, -1)
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.draw_pos[X] + player.width <= SCREEN_WIDTH:
                player.move(X, 1)

            bomb_list[0].move(options.mute)
            bomb_list[1].move(options.mute)

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

        # Update if Game is Over
        else:
            pygame.mixer.music.stop()

        ##########
        # Update Display
        ##########
        # Always Display
        screen.fill("black")
        screen.blit(background, (0,0))

        # Display while Game is being played
        if not game_over:
            for i in treasure_list:
                screen.blit(i.image, [i.draw_pos[X], i.draw_pos[Y]])
            screen.blit(player.image, [player.draw_pos[X], player.draw_pos[Y]])

            screen.blit(bomb_list[0].image, [bomb_list[0].draw_pos[X], bomb_list[0].draw_pos[Y]])
            screen.blit(bomb_list[1].image, [bomb_list[1].draw_pos[X], bomb_list[1].draw_pos[Y]])

        # Display while Game is Over
        else:
            if options.options_menu:
                if options.mute:
                    mute_status_message = pygame.font.SysFont("timesnewroman", 75).render("Mute = on", True, "gold")
                else:
                    mute_status_message = pygame.font.SysFont("timesnewroman", 75).render("Mute = off", True, "gold")
                screen.blit(mute_status_message, [125, 100])
            else:
                screen.blit(
                        # Idk how to make the next three lines not be ugly
                        pygame.font.SysFont("timesnewroman", 100).render(
                            "Game Over", True, color),
                        [100, 100])
                screen.blit(message, [100, 250])
                screen.blit(pygame.font.SysFont("timesnewroman", 60).render(
                    "Press o for options", True, color),
                            [100, 400])

        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


if __name__ == "__main__":
    main()

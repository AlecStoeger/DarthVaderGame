class Options:
    def __init__(self, game_engine, screen):
        self.options_menu = False
        self.mute = True
        self.options = [
                [self.mute, "Mute"]
        ]
        self.screen = screen
        self.game_engine = game_engine

    # Change this out with using option = not option
    def toggle(self, option):
        if option:
            option = False
        else:
            option = True
        return option

    def play_sound(self, callback, sound):
        if not self.mute:
            callback(sound)

    def display_menu(self):
        for option in self.options:
            if option[0]:
                option_status_message = self.game_engine.font\
                        .SysFont("timesnewroman", 75)\
                        .render(f"{option[1]} = true", True, "gold")
            else:
                option_status_message = self.game_engine.font\
                        .SysFont("timesnewroman", 75)\
                        .render(f"{option[1]} = false", True, "gold")
            self.screen.blit(option_status_message, [125, 100])

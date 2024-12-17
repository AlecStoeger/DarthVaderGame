class Options:
    def __init__(self):
        self.options_menu = False
        self.mute = True
        self.options = [
                self.mute
        ]

    def toggle(self, option):
        if option:
            option = False
        else:
            option = True
        return option

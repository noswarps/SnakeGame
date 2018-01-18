from Snake.color import Color


class StartMenu:

    def __init__(self, padding=20, screen_width=500, screen_height=500, bg_color=Color.silver, button_color=Color.blue,
                 font_color=Color.black):
        self.width = screen_width - padding * 2
        self.height = screen_height - padding * 2
        self.x, self.y = padding, padding
        self.bg_color = bg_color
        self.buttons = [Button(caption='PLAY'), Button(caption='SCORES')]
        for button in self.buttons:
            button.determine_button_dim(self.buttons.index(button), self.width, self.height, padding_x=50,
                                        padding_y=150, button_space=25, font_padding=5, menu_x=self.x, menu_y=self.y)

    @property
    def pos(self):
        return self.x, self.y

    @property
    def size(self):
        return self.width, self.height


class Button:

    def __init__(self, caption=None, color=Color.black, font_color=Color.white):
        self.caption = caption
        self.color = color
        self.font_color = font_color
        self.x, self.y, self.height, self.width = None, None, None, None
        self.font = None
        self.font_size = None
        self.clicked = False

    def determine_button_dim(self, index, menu_width, menu_height, padding_x, padding_y, button_space,
                             font_padding, menu_x, menu_y):
        self.width = menu_width - padding_x * 2
        self.height = menu_height // 10
        self.x = menu_x + padding_x
        self.y = menu_y + padding_y + (index * (self.height + button_space))
        self.font_size = self.height - font_padding * 2

    def is_on(self, position):
        return position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height)

    @property
    def pos(self):
        return self.x, self.y

    @property
    def size(self):
        return self.width, self.height

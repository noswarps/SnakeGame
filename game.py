from Snake.color import Color
from Snake.snake import Snake
from Snake.food import Food
from Snake.startmenu import StartMenu
import pygame as pg


class Game:

    def __init__(self, height=500, width=500, color=Color.black, caption='Snake Game', fps=20,
                 snake_size=10, snake_colour=Color.green, snake_start_pos=(0, 0), start_direction='right',
                 food_color=Color.red):

        self.height, self.width = height, width
        self.color = color
        self.caption = caption
        self.fps = fps
        self.playing = False
        self.running = True

        pg.init()
        self.display = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.caption)
        self.clock = pg.time.Clock()

        self.snake = Snake(size=snake_size, x=snake_start_pos[0], y=snake_start_pos[1], color=snake_colour,
                           direction=start_direction)
        self.food = Food(color=food_color, screen_width=width, screen_height=height, size=snake_size)

        self.menu = StartMenu(padding=20, screen_width=width, screen_height=height)

    def loop(self):

        while self.running:

            self._click_listener()
            self._menu_render()

            while self.playing:

                self.input_listener()
                self._backend_logic()
                self._render()
                self.clock.tick(self.fps)


        pg.quit()
        quit()

    def input_listener(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing, self.running = False

            if event.type == pg.KEYDOWN:
                if self.snake.direction[0] != 0:
                    if pg.key.get_pressed()[pg.K_UP]:
                        self.snake.change_direction('up')
                    elif pg.key.get_pressed()[pg.K_DOWN]:
                        self.snake.change_direction('down')
                elif self.snake.direction[1] != 0:
                    if pg.key.get_pressed()[pg.K_LEFT]:
                        self.snake.change_direction('left')
                    elif pg.key.get_pressed()[pg.K_RIGHT]:
                        self.snake.change_direction('right')

    def _backend_logic(self):
        if self.snake.is_at(self.food.x, self.food.y):
            self.snake.grow()
            self.food.move()

        for bodypart in self.snake[:len(self.snake) - 1]:
            if self.snake.is_at(bodypart.x, bodypart.y):
                self.playing = False

        if self.snake.x not in range(0, self.width, self.snake.width):
            self.playing = False

        if self.snake.y not in range(0, self.height, self.snake.height):
            self.playing = False

        self.snake.move()

    def _render(self):
        self.display.fill(self.color)

        pg.draw.rect(self.display, self.food.color, pg.Rect(self.food.pos, self.food.size))

        for part in self.snake:
            pg.draw.rect(self.display, self.snake.color, pg.Rect(part.pos, self.snake.size))

        pg.display.update()

    def _click_listener(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running, self.playing = False, False
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    pos = pg.mouse.get_pos()
                    if self.menu.buttons[0].is_on(pos):
                        self.playing = True
                        self.snake.reset()

    def _menu_render(self):

        self.display.fill(self.color)
        pg.draw.rect(self.display, self.menu.bg_color, pg.Rect(self.menu.pos, self.menu.size))

        for button in self.menu.buttons:
            pg.draw.rect(self.display, button.color, pg.Rect(button.pos, button.size))
            font = pg.font.Font(None, button.font_size)
            text = font.render(button.caption, True, Color.red)
            self.display.blit(text, (button.x + (button.width - text.get_width()) / 2, button.y + (button.height - text.get_height()) / 2))

        pg.display.update()

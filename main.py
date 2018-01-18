from Snake.game import Game


def main():
    game = Game(fps=25, snake_size=15, height=480, width=480)
    game.loop()

if __name__ == '__main__':
    main()
from Snake.color import Color


class Snake:

    def __init__(self, size=10, x=0, y=0, color=Color.green, direction='right'):
        self._directions = {'left': (-size, 0), 'right': (size, 0), 'up': (0, -size), 'down': (0, size)}
        self.direction = self._directions[direction]
        self.color = color
        self.height, self.width = size, size
        self.body = [SnakeBodyPart(x, y, self.direction)]

    def move(self):
        for i in range(len(self)):
            try:
                self[i].direction = self[i+1].direction
            except IndexError:
                self[i].direction = self.direction
            self[i].move()

    def is_at(self, x, y):
        return self[-1].x == x and self[-1].y == y

    def grow(self):
        self.body.insert(0, SnakeBodyPart(self[0].x - self[0].direction[0], self[0].y - self[0].direction[1], self[0].direction))

    def change_direction(self, direction):
        self.direction = self._directions[direction]

    def reset(self):
        self.body = [SnakeBodyPart(0, 0, self._directions['right'])]
        self.change_direction('right')

    @property
    def pos(self):
        return self[-1].x, self[-1]. y

    @property
    def x(self):
        return self[-1].x

    @property
    def y(self):
        return self[-1].y

    @property
    def size(self):
        return self.width, self.height

    def __iter__(self):
        for part in self.body:
            yield part

    def __getitem__(self, item):
        return self.body[item]

    def __len__(self):
        return len(self.body)


class SnakeBodyPart:

    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.direction = direction

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    @property
    def pos(self):
        return self.x, self.y




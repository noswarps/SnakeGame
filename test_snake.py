from unittest import TestCase
from Snake.snake import Snake


class TestSnake(TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_move(self):
        self.snake.move()
        self.assertTupleEqual(self.snake.pos, (10, 0))
        self.snake.grow()
        self.assertTupleEqual(self.snake[0].pos, (0, 0))
        self.snake.move()
        self.assertTupleEqual(self.snake[0].pos, (10, 0))
        self.snake.move()
        self.assertTupleEqual(self.snake[0].pos, (20, 0))


    def test_is_at(self):
        self.assertEqual(self.snake.is_at(0, 0), True)
        self.assertEqual(self.snake.is_at(10, 0), False)
        self.snake.move()
        self.assertEqual(self.snake.is_at(10, 0), True)
        self.assertEqual(self.snake.is_at(0, 0), False)

    def test_grow(self):
        self.assertEqual(len(self.snake), 1)
        self.snake.grow()
        self.assertEqual(len(self.snake), 2)
        self.assertTupleEqual(self.snake[0].pos, (-10, 0))

    def test_pos(self):
        for i in range(20):
            self.snake.move()
        self.assertTupleEqual(self.snake.pos, (200, 0))

    def test_size(self):
        self.assertTupleEqual(self.snake.size, (10, 10))

    def test_change_direction(self):
        self.snake.change_direction('down')
        self.assertTupleEqual(self.snake.direction, (0, 10))
        self.snake.move()
        self.assertTupleEqual(self.snake.pos, (0, 10))

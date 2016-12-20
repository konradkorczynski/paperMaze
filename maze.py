from random import shuffle, randrange
import sys


class Maze:
    def __init__(self, width=10, height=10):
        self.maze = []
        self.width = width
        self.height = height

        if width < 2 or height < 2:
            raise ValueError("Please make sure width and height are at least 2.")

        sys.setrecursionlimit(100000)

        for h in range(0, self.height):
            row = []
            for w in range(0, self.width):
                row.append([0, 1, 1])
            self.maze.append(row)

        for cell in self.maze[-1]:
            cell[1] = 0

        for row in self.maze:
            row[-1][2] = 0

        start_x = randrange(width)
        start_y = randrange(height)
        self.walk_maze(start_x, start_y)

    def walk_maze(self, x, y):
        self.maze[y][x][0] = 1
        next_cell = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(next_cell)

        for (next_cell_x, next_cell_y) in next_cell:
            if next_cell_y > self.height - 1 or next_cell_x > self.width - 1 or next_cell_y < 0 or next_cell_x < 0 or \
                    self.maze[next_cell_y][next_cell_x][0]:
                continue
            if next_cell_x > x:
                self.maze[y][x][2] = 0
            if next_cell_x < x:
                self.maze[next_cell_y][next_cell_x][2] = 0
            if next_cell_y > y:
                self.maze[y][x][1] = 0
            if next_cell_y < y:
                self.maze[next_cell_y][next_cell_x][1] = 0
            self.walk_maze(next_cell_x, next_cell_y)

from random import shuffle, randrange


class Maze:
    def __init__(self, width=10, height=10):
        self.maze = []
        self.width = width
        self.height = height
        self.count_of_cells = width * height

        if width < 2 or height < 2:
            raise ValueError("Please make sure width and height are at least 2.")

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
        cells = [[start_x, start_y]]
        self.walk_maze_loop(cells)

    def walk_maze_loop(self, cells):
        while cells:
            index = len(cells) - 1
            x, y = cells[index]
            self.maze[y][x][0] = 1
            next_cells = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(next_cells)
            for next_cell in next_cells:
                next_cell_x, next_cell_y = next_cell
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
                self.maze[next_cell_y][next_cell_x][0] = 1
                cells.append([next_cell_x, next_cell_y])
                index = None
                break
            if index is not None:
                del cells[index]

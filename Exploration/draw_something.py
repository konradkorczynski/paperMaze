from datetime import datetime
from random import shuffle, randrange
import sys
import cairo

sys.setrecursionlimit(100000)
height = 100
width = int(height * 1.414)
border = 40
wall_thickness = 120 / float(height)
if wall_thickness < 4:
    wall_thickness = 4
filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
a4_width, a4_height = 3508, 2480
cell_height = (a4_height - border) / float(height)
cell_width = (a4_width - border) / float(width)

surface = cairo.PDFSurface("a4_maze_" + str(height) + "_" + filename + ".pdf", a4_width, a4_height)
ctx = cairo.Context(surface)

# draw background and border
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.set_source_rgb(0, 0, 0)
ctx.move_to(0, 0)
ctx.line_to(a4_width, 0)
ctx.line_to(a4_width, a4_height)
ctx.line_to(0, a4_height)
ctx.line_to(0, 0)
ctx.set_line_width(border)
ctx.stroke()
ctx.set_line_width(0)
ctx.set_source_rgb(0.2, 0.87, 0.3)
ctx.rectangle(border / 2 + 1, a4_height - (border / 2) - cell_height + 1, cell_width - 2, cell_height - 2)
ctx.fill()
ctx.set_source_rgb(1, 0.28, 0.28)
ctx.rectangle(a4_width - (border / 2) - cell_width + 1, border / 2 + 1, cell_width - 2, cell_height - 2)
ctx.fill()

# prepare maze
maze = []
for h in range(0, height):
    row = []
    for w in range(0, width):
        row.append([0, 1, 1])
    maze.append(row)

for cell in maze[-1]:
    cell[1] = 0

for row in maze:
    row[-1][2] = 0


def walk_maze(x, y):
    maze[y][x][0] = 1
    next_cell = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    shuffle(next_cell)

    for (next_cell_x, next_cell_y) in next_cell:
        if next_cell_y > height - 1 or next_cell_x > width - 1 or next_cell_y < 0 or next_cell_x < 0 or \
                maze[next_cell_y][next_cell_x][0]:
            continue
        if next_cell_x > x:
            maze[y][x][2] = 0
        if next_cell_x < x:
            maze[next_cell_y][next_cell_x][2] = 0
        if next_cell_y > y:
            maze[y][x][1] = 0
        if next_cell_y < y:
            maze[next_cell_y][next_cell_x][1] = 0
        walk_maze(next_cell_x, next_cell_y)


start_x = randrange(width)
start_y = randrange(height)
walk_maze(start_x, start_y)

# drawing bit
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(wall_thickness)
row_count = 0
for row in maze:
    cell_count = 0
    for cell in row:
        cell_top_position = [cell_count * cell_width + border / 2, row_count * cell_height + border / 2]
        if cell[1]:
            ctx.move_to(cell_top_position[0], cell_top_position[1] + cell_height)
            ctx.line_to(cell_top_position[0] + cell_width, cell_top_position[1] + cell_height)
            ctx.stroke()
        if cell[2]:
            ctx.move_to(cell_top_position[0] + cell_width, cell_top_position[1])
            ctx.line_to(cell_top_position[0] + cell_width, cell_top_position[1] + cell_height)
            ctx.stroke()
        cell_count += 1
    row_count += 1

ctx.show_page()

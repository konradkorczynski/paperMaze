import maze
import maze_painter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--complexity', action="store", default=0, type=int,
                    help='How complex the maze is to be.')
parser.add_argument('-n', '--number', action="store", default=0, type=int, help='How many mazes to create.')
args = parser.parse_args()

number_of_mazes = args.number
height = args.complexity

while True:
    if height < 2 or height > 90:
        height = raw_input("Complexity of maze (2-90 [above 50 might cause crashes]): ")
        height = int(height) if len(height) > 0 else 0
    else:
        break

while True:
    if number_of_mazes < 1:
        number_of_mazes = raw_input("Number of mazes to generate: ")
        number_of_mazes = int(number_of_mazes) if len(number_of_mazes) > 0 else 0
    else:
        break

width = int(height * 1.414)
painter = maze_painter.MazePainter()

for i in range(0, number_of_mazes):
    new_maze = maze.Maze(width, height)
    painter.paint_maze(new_maze, i)

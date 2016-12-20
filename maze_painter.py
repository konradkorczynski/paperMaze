from datetime import datetime
import cairo


class MazePainter:
    def __init__(self):
        pass

    @staticmethod
    def paint_maze(maze, number):
        border = 40
        wall_thickness = 120 / float(maze.height)
        if wall_thickness < 4:
            wall_thickness = 4
        filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        a4_width, a4_height = 3508, 2480
        cell_height = (a4_height - border) / float(maze.height)
        cell_width = (a4_width - border) / float(maze.width)

        surface = cairo.PDFSurface("a4_maze_" + str(maze.height) + "_" + str(number) + "_" + filename + ".pdf", a4_width, a4_height)
        ctx = cairo.Context(surface)

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

        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(wall_thickness)
        row_count = 0
        for row in maze.maze:
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
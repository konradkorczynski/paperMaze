import cairo
import math

a4_width, a4_height = 3508, 2480
width, height = 768, 768
surface = cairo.PDFSurface("circle.pdf", a4_width, a4_height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()
ctx.set_source_rgb(0, 0, 0)
ctx.move_to(0, 0)
ctx.line_to(3508, 2480)
ctx.set_line_width(0.2)
ctx.stroke()
ctx.show_page()

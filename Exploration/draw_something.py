import math, cairo

width, height = 768, 768
surface = cairo.PDFSurface("circle.pdf", width, height)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(0, 0, width, height)
ctx.fill()
ctx.set_source_rgb(1, 0, 0)
ctx.move_to(width / 2, height / 2)
ctx.arc(width / 2, height / 2, 512 * 0.25, 0, math.pi * 2)
ctx.fill()
ctx.show_page()

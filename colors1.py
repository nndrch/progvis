# amostras de cor

colormode(CMYK)
size(520, 352)

d1 = 4
d2 = 4
d3 = 8

if d1 <= 0: d1 = 1
if d2 <= 0: d2 = 1
if d3 <= 0: d3 = 1

dist = 0
x, y = 0, 0

cell_width = float(WIDTH) / d1
cell_height = float(HEIGHT) / d2

c1_step = 1.00 / d1
c2_step = 1.00 / d2
c3_step = 1.00 / d3

c1_invert = False
c2_invert = False
c3_invert = True

for i in range(d1):
    for j in range(d2):
        _x = x + (i * (dist + cell_width))
        _y = y + (j * (dist + cell_height))
        c1 = i * c1_step
        c2 = j * c2_step
        if c1_invert:
            c1 = 1.00 - c1
        if c1_invert:
            c2 = 1.00 - c2
        for k in range(d3):
            c3 = (k) * c3_step
            if c3_invert:
                c3 = 1.00 - c3
            _w = cell_width / d3
            _h = cell_height / d3
            _cell_width = cell_width - (k * _w)
            _cell_height = cell_height - (k * _h)
            _color = color(c1, c3, c2, 0)
            fill(_color)
            rect(_x, _y, cell_width, _cell_height)

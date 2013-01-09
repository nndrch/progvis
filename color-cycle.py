# simple color cycle

x, y = 0, 0
w = h = 8
c = 9
s = 64

# make colors

_colors = []
for i in range(c):
    _color = color(random(), random(), random())
    _colors.append(_color)

# draw

size(w*s, h*s)

_x, _y = x, y

_count = 0
for i in range(len(_colors)):
    for j in range(len(_colors)):
        _index = _count % w
        c = _colors[_index]
        fill(c)
        rect(_x, _y, s, s)
        _x += s
        _count += 1
    _x = x
    _y += s

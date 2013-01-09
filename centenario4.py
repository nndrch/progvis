# marca centenario RJ

# functions

def draw_lines(points, t):
    # set state
    autoclosepath(True)
    nofill()
    stroke(0)
    strokewidth(t)
    # draw
    beginpath()
    _moveto = True
    for point in points:
        x, y = point
        if _moveto:
            moveto(x, y)
            _moveto = False
        else:
            lineto(x, y)
    endpath()

def draw_points(points, point_size):
    # set state
    fill(1, 0, 0)
    nostroke()
    # draw
    for point in points:
        x, y = point
        oval(x-(point_size/2), y-(point_size/2), point_size, point_size)

# parameters

w = h = 448
x, y = w/2, h/2
d = 48
axis = 158
s = 22
t = 23

_draw_points = True

# points

_points = [
    ( x - axis,   y - d ),
    ( x + axis,   y - d ),
    ( x + d,      y - axis ),
    ( x + d,      y + axis ),
    ( x + axis,   y + d ),
    ( x - axis,   y + d ),
    ( x - d,      y + axis ),
    ( x - d,      y - axis ),
]

# draw

size(w, h)

draw_lines(_points, t)

if _draw_points:
    draw_points(_points, s)

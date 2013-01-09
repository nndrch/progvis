# module

def draw_module(pos, s, w, r):
    x, y = pos
    # background element
    fill(1, 0, 0)
    rect(x, y, s, s)
    # cross element
    nofill()
    stroke(1)
    strokewidth(w)
    line(x + (s/2), y, x + s/2, y + s)
    line(x, y + (s/2), x + s, y + s/2)
    # small squares
    nostroke()
    fill(1, 1, 0)
    rect(x, y, r, r)
    rect(x + (s-r), y, r, r)
    rect(x, y + (s-r), r, r)
    rect(x + (s-r), y + (s-r), r, r)

# parameters

_x, _y = 77, 88

_s = 71
_w = 9
_r = 12

# draw

size(300, 300)
background(.3)

draw_module((_x, _y), _s, _w, _r)

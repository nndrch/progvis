# module

from math import cos, sin

def draw_module(pos, s, w, r):
    x, y = pos
    # background element
    fill(1, 0, 0)
    rect(x, y, s, s)
    # cross element
    nofill()
    stroke(0, 1, 0)
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

_x, _y = 0, 0

_s = 54
_w = 40
_r = 8

_amount = 7
_spacing = 2

# draw

_canvas = _s * _amount + ( (_amount-1) * _spacing)

size(_canvas, _canvas)
background(0, .5, 1)

x_ = _x

for i in range(_amount):
    for j in range(_amount):
        r_ = 4 + (j * sin(_r))
        w_ = 10 - (i * cos(_w))
        draw_module((x_, _y), _s, w_, r_)
        x_ += _s + _spacing
    _y += _s + _spacing
    x_ = _x

# triangulo : modulo

def draw_module(x, y, w, h):
    fill(0)
    nostroke()
    beginpath(x, y)
    lineto(x, y + w)
    lineto(x + h, y + w)
    endpath()

_x = _y = 0
_w = _h = 20

draw_module(_x, _y, _w, _h)

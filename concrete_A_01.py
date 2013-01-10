# modulo 1

def draw_module(pos, s, w, r):
    x, y = pos
    # fundo
    fill(1, 0, 0)
    rect(x, y, s, s)
    # cruz
    nofill()
    stroke(1)
    strokewidth(w)
    line(x + (s/2), y, x + s/2, y + s)
    line(x, y + (s/2), x + s, y + s/2)
    # quadrados
    nostroke()
    fill(1, 1, 0)
    rect(x, y, r, r)
    rect(x + (s-r), y, r, r)
    rect(x, y + (s-r), r, r)
    rect(x + (s-r), y + (s-r), r, r)

# parametros

_x, _y = 86, 92

_s = 74
_w = 17
_r = 19

# desenha

size(300, 300)
background(.3)

draw_module((_x, _y), _s, _w, _r)

# marca centenario RJ

# parametros

x, y = 30, 30
d = 46
axis = 163
s = 22

# pontos

x += axis
y += axis

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

# draw lines

autoclosepath(True)
nofill()
stroke(.5)
strokewidth(10)

beginpath()
_moveto = True
for point in _points:
    x, y = point
    if _moveto:
        moveto(x, y)
        _moveto = False
    else:
        lineto(x, y)
endpath()

# draw points

fill(0)
nostroke()

#for point in _points:
#    x, y = point
#    oval(x-(s/2), y-(s/2), s, s)

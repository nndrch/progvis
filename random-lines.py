# line connecting random points

size(400, 400)

_margin = 76
_points = 49

beginpath()

for i in range(_points):
    x = random(_margin, WIDTH - _margin)
    y = random(_margin, HEIGHT - _margin)
    if i == 0:    
        moveto(x, y)
    else:
        lineto(x, y)

p = endpath(draw=False)

nofill()
stroke(random(), random(), random())
strokewidth(2)

drawpath(p)
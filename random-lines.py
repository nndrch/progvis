# linhas conectando pontos aleatorios

size(400, 400)
autoclosepath(False)

_margin = 40
_points = 20

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
strokewidth(random(2, 10))

drawpath(p)
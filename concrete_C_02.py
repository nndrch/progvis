# triangulos : composition
# homage to Anni Albers

w = 45
x, y = 0, 0
a = 12

size(w*a, w*a)
background(1)
fill(0)

for i in range(a):
    for j in range(a):
        push()
        # rotaciona aleatoriamente
        r = random()
        if r < .25:         rotate(90)
        elif .25 < r < .5:  rotate(180)
        elif .5 < r < .75:  rotate(270)
        else:               rotate(360)
        # desenha triangulo
        beginpath(x, y)
        lineto(x + w, y)
        lineto(x, y + w)
        endpath()        
        pop()
        # move coluna (x)
        x += w
    # move linha (y)
    x = 0
    y += w

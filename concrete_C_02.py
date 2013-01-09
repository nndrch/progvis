# Anni Albers recreated

w = 12
x, y = 0, 0
a = 30

size(w*a, w*a)
background(1, 0, 0)
fill(0, 0, 1)

for i in range(a):
    for j in range(a):
        push()
        # rotate
        r = random()
        if r < .25:
            rotate(90)
        elif .25 < r < .5:
            rotate(180)
        elif .5 < r < .75:
            rotate(270)
        else:
            rotate(360)
        # draw triangle
        beginpath(x, y)
        lineto(x + w, y)
        lineto(x, y + w)
        endpath()        
        pop()
        # move column
        x += w
    # move row
    x = 0
    y += w

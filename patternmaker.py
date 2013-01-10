# [h] variable modules

# functions

def modulo((x, y), state):
    # module colors
    if state == 0:
        c = color(1, 0, 0, 0)
    elif state == 1:
        c = color(0, 1, 0, 0)
    elif state == 2:
        c = color(0, 0, 1, 0)
    elif state == 3:
        c = color(0, 0, 0, 3)
    else:
        print "error"
    c.alpha = random()
    fill(c)
    # module shape
    n = random()
    if n < .5:
        oval(x, y, module, module)
    else:
        rect(x, y, module, module)

# settings

colormode(CMYK)
size(400, 300)

module = 20
cols = WIDTH / module
rows = HEIGHT / module
_x = 0
_y = 0

# draw!

for i in range(cols):
    for j in range(rows):
        pos_x = _x + (i * module)
        pos_y = _y + (j * module)
        modulo((pos_x, pos_y), random(0,3))

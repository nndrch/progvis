# [h] variable modules

colors = ximport('colors')

#-----------
# functions
#-----------

def modulo((x, y), state):
    # module colors
    if state == 0:
        c = colors.cmyk(1, 0, 0, 0)
    elif state == 1:
        c = colors.cmyk(0, 1, 0, 0)
    elif state == 2:
        c = colors.cmyk(0, 0, 1, 0)
    elif state == 3:
        c = colors.cmyk(0, 0, 0, 3)
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

#----------
# settings
#----------

# colormode(CMYK)
size(800, 600)

module = 34
cols = WIDTH / module
rows = HEIGHT / module
_x = 0
_y = 0

#-------
# draw!
#-------

for i in range(cols):
    for j in range(rows):
        pos_x = _x + (i * module)
        pos_y = _y + (j * module)
        modulo((pos_x, pos_y), random(0,3))

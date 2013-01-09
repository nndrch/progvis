# [h] simple animation with sin

from math import sin, radians

colors = ximport('colors')

def _draw_background(hue):
    _color = colors.hsb(hue, .5, .2)
    background(_color)

def _draw_cross(x, y, hue):
    _color = colors.hsb(hue, 1, .8, .5)
    stroke(_color)
    strokewidth(1)
    line(x, 0, x, HEIGHT, draw=True)
    line(0, y, WIDTH, y, draw=True)

def _draw_circle(x, y, hue, v):
    nostroke()
    _color = colors.hsb(hue, 1, .5)
    fill(_color)
    w = (WIDTH/2) - v
    h = (WIDTH/2) - v
    oval(x - (w/2), y - (w/2), w, w)

def _draw_wave(x, y, hue, v):
    nostroke()
    _color = colors.hsb(hue, 1, 1)
    _size = 10
    fill(_color)
    _y = abs(v * 2) - (_size/2)
    _x = x - (_size/2)
    push()
    rotate(frame * 10)
    rect(_x, _y, _size, _size)
    pop()

def setup():
    global frame, x, y
    frame = 1
    x, y = 0, HEIGHT/2
    
def draw():

    global frame, x, y

    _x = WIDTH/2
    _y = HEIGHT/2
    s = sin(radians(frame))
    hue = abs(s) * .5
    _var = s * (WIDTH / 2)
    _y += _var

    _draw_background(hue)
    _draw_cross(_x, _y, hue)
    _draw_circle(_x, _y, hue, _var)
    _draw_wave(_x, _y, hue, _var)

    frame += 1
    _x += 1

#------
# run!
#------

size(600, 600)
speed(100)

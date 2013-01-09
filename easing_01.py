# [h] simple animation with sin

from math import sin, radians

colors = ximport('colors')

def _draw_background(frame):
    s = sin(radians(frame))
    hue = abs(s) * .5
    _color = colors.hsb(hue, .5, .2)
    background(_color)

def _draw_cross(frame):
    x = WIDTH/2
    y = HEIGHT/2
    s = sin(radians(frame))
    hue = abs(s) * .5
    v = s * (HEIGHT / 2)
    y += v
    _color = colors.hsb(hue, 1, .8, .5)
    stroke(_color)
    strokewidth(1)
    line(x, 0, x, HEIGHT, draw=True)
    line(0, y, WIDTH, y, draw=True)

def _draw_circle(frame):
    x = WIDTH/2
    y = HEIGHT/2
    s = sin(radians(frame))
    hue = abs(s) * .5
    v = s * (HEIGHT / 2)
    y += v
    nostroke()
    _color = colors.hsb(hue, 1, .7, .7)
    fill(_color)
    w = (WIDTH/2) - v
    h = (WIDTH/2) - v
    oval(x - (w/2), y - (w/2), w, w)

def _draw_rotate(frame):
    x, y = WIDTH/2, HEIGHT/2
    s = sin(radians(frame))
    hue = abs(s) * .5
    v = s * (HEIGHT / 2)
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
    y += v

def _draw_wave(frame):
    counts = frame // WIDTH
    x = frame - (counts * WIDTH)
    s = sin(radians(frame))
    hue = abs(s) * .5
    _size = 2 + (6 * hue)
    y = (HEIGHT/2) - ( s * (HEIGHT / 4) ) - (_size/2)
    _color = colors.hsb(hue, 0, 1, .35)
    # draw
    nostroke()
    fill(_color)
    oval(x, y, _size, _size, draw=True)

def setup():
    global frame
    frame = 1
    
def draw():
    global frame
    _draw_background(frame)
    _draw_cross(frame)
    _draw_circle(frame)
    _draw_rotate(frame)
    # wave
    _trail = WIDTH/3
    _interval = 8
    for i in range(frame-_trail, frame+_trail, _interval):
        _draw_wave(i)
    # done
    frame += 1

#------
# run!
#------

size(400, 300)
speed(100)

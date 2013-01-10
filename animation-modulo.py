# minimal animation

size(300, 300)
speed(30)

def draw():
    x = FRAME % WIDTH
    stroke(1, 0, 0)
    line(x, 0, x, HEIGHT)

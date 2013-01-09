
size(300, 300)
speed(30)

def setup():
    global frame
    frame = 0

def draw():
    global frame
    x = frame % WIDTH
    fill(1, 0, 0)
    rect(x, 0, 1, HEIGHT)
    frame += 1

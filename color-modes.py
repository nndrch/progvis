# color modes

size(300, 100)

x = y = 20
fill(.5)
rect(x - 5, y - 5, 40, 40)
fill(.5, .5)
rect(x + 5, y + 5, 40, 40)

x += 60
colormode(RGB)
fill(1, 0, 0)
rect(x - 5, y - 5, 40, 40)
fill(1, 0, 0, .5)
rect(x + 5, y + 5, 40, 40)

x += 60
colormode(HSB, range=255)
fill(255, 255, 255)
rect(x - 5, y - 5, 40, 40)
fill(255, 255, 255, 127)
rect(x + 5, y + 5, 40, 40)

x += 60
colormode(CMYK, range=100)
fill(0, 100, 100, 0)
rect(x - 5, y - 5, 40, 40)
fill(0, 100, 100, 0, 50)
rect(x + 5, y + 5, 40, 40)

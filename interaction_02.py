size(400, 400)
speed(20)
 
def setup():
    pass

def draw():    
    if mousedown:
        background(1, 1, 0, .05)
        fill(1, 1, 0, .5)
        rect(20, 20, 100, 100)
        for i in range(10):
            fill(random(), random(), random(), .3)
            var_pos = 60
            var_size = 80
            var_posx = random(-var_pos, var_pos)
            var_posy = random(-var_pos, var_pos)
            var_size = random(var_size/5, var_size)
            oval(MOUSEX + var_posx, MOUSEY + var_posy, var_size, var_size)
    else:
        background(.2)
        fill(.8)
        rect(20, 20, 100, 100)

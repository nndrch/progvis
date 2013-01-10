size(600, 600)
background(.8)

nofill()
strokewidth(7)
autoclosepath(False)

p1_x = 96
p1_y = 76
p2 = 193, 220
p3_a = 362, 165
p3_b = 466, 361
p3_c = 351, 506

oval_size = 52

# contorno
stroke(0, 1, 0)
beginpath()
moveto(p1_x, p1_y)
lineto(p2[0], p2[1])
curveto(p3_a[0], p3_a[1], p3_b[0], p3_b[1], p3_c[0], p3_c[1])
endpath()

# pontos moveto + lineto
stroke(0, 0, 1)
oval(p1_x - oval_size/2, p1_y - oval_size/2, oval_size, oval_size)      # p1
oval(p2[0] - oval_size/2, p2[1] - oval_size/2, oval_size, oval_size)    # p2

# pontos curveto:
# primeira alça do segmento bezier (p3_a)
stroke(1, 0, 0)
line(p2[0], p2[1], p3_a[0], p3_a[1])
oval(p3_a[0] - oval_size/2, p3_a[1] - oval_size/2, oval_size, oval_size)

# segunda alça do segmento bezier (p3_b)
line(p3_c[0], p3_c[1], p3_b[0], p3_b[1])
oval(p3_b[0] - oval_size/2, p3_b[1] - oval_size/2, oval_size, oval_size)

# último ponto do segmento bezier (p3_c)
# stroke(0, 0, 1)
oval(p3_c[0] - oval_size/2, p3_c[1] - oval_size/2, oval_size, oval_size)

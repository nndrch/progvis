# exemplo de construção de curva bezier

def mark_pos(x, y, s, c):
    stroke(c)
    oval(x - s/2, y - s/2, s, s)

size(600, 600)
background(.8)

nofill()
strokewidth(7)
autoclosepath(False)

p1_x = 96
p1_y = 76
p2 = 198, 232
p3_a = 362, 165
p3_b = 466, 360
p3_c = 351, 502

oval_size = 44

# bezier
stroke(0, 1, 0)
beginpath()
moveto(p1_x, p1_y)
lineto(p2[0], p2[1])
curveto(p3_a[0], p3_a[1], p3_b[0], p3_b[1], p3_c[0], p3_c[1])
p = endpath(draw=True)

# ponto moveto (p1)
mark_pos(p1_x, p1_y, oval_size, color(0, 0, 1))

# ponto lineto (p2)
mark_pos(p2[0], p2[1], oval_size, color(0, 0, 1))

# pontos curveto (p3)
mark_pos(p3_a[0], p3_a[1], oval_size, color(0, 1, 1))
mark_pos(p3_b[0], p3_b[1], oval_size, color(0, 1, 1))
mark_pos(p3_c[0], p3_c[1], oval_size, color(1, 0, 1))

# alavancas de controle
stroke(1, 0, 0)
line(p2[0], p2[1], p3_a[0], p3_a[1])
line(p3_c[0], p3_c[1], p3_b[0], p3_b[1])

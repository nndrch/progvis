# calcular o centro do retangulo

w, h = 320, 333
x, y = 61, 92

rect(x, y, w, h)

center_x = x + (w / 2)
center_y = y + (h / 2)

L = 54

strokewidth(2)
stroke(1, 0, 0)
line(center_x, center_y - L, center_x, center_y + L)
line(center_x - L, center_y, center_x + L, center_y)

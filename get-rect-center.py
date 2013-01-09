# [h] get center of rectangle

w, h = 239, 358
x, y = 122, 80

rect(x, y, w, h)

center_x = x + (w / 2)
center_y = y + h / 2

L = 38

strokewidth(2)
stroke(1, 0, 0)
line(center_x, center_y - L, center_x, center_y + L)
line(center_x - L, center_y, center_x + L, center_y)
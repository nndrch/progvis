# marca centenario RJ

x, y = 213, 279
d = 43
axis = 157

autoclosepath(False)
nofill()
stroke(.5)
strokewidth(5)

line(x - d, y - axis, x - d, y + axis)
line(x + d, y - axis, x + d, y + axis)
line(x - axis, y - d, x + axis, y - d)
line(x - axis, y + d, x + axis, y + d)

line(x + d, y + axis, x + axis, y + d)
line(x - d, y + axis, x - axis, y + d)
line(x + d, y - axis, x + axis, y - d)
line(x - d, y - axis, x - axis, y - d)

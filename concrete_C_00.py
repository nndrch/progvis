# triangulo

x, y = 20, 20
w = h = 40

fill(0)
nostroke()

beginpath(x, y)
lineto(x, y + w)
lineto(x + h, y + w)
endpath()
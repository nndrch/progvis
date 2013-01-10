# modulo 1

s = 57
w = 15
r = 13

# background element
fill(1, 0, 0)
rect(0, 0, s, s)

# cross element
nofill()
stroke(1)
strokewidth(w)
line(s/2, 0, s/2, s)
line(0, s/2, s, s/2)

# small squares
nostroke()
fill(1, 1, 0)
rect(0, 0, r, r)
rect(s-r, 0, r, r)
rect(0, s-r, r, r)
rect(s-r, s-r, r, r)

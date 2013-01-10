# exemplo de formas compostas

# http://nodebox.net/code/index.php/Compound_paths

size(600, 400)
nofill()
strokewidth(3)

# união

x, y = 40, 20

nofill()
stroke(.8)
path1 = oval(x + 40, y + 40, 80, 80, draw=True)
path2 = oval(x + 90, y + 40, 80, 80, draw=True)
compound = path1.union(path2)
fill(.8, .5)
stroke(0)
drawpath(compound)

# interseção

x, y = 280, 20

nofill()
stroke(.8)
path1 = oval(x + 40, y + 40, 80, 80, draw=True)
path2 = oval(x + 90, y + 40, 80, 80, draw=True)
compound = path1.intersect(path2)
stroke(0)
fill(.8, .5)
drawpath(compound)

# diferença

x, y = 40, 200

nofill()
stroke(.8)
path1 = oval(x + 40, y + 40, 80, 80, draw=True)
path2 = oval(x + 90, y + 40, 80, 80, draw=True)
compound = path1.difference(path2)
stroke(0)
fill(.8, .5)
drawpath(compound)

# xor

x, y = 280, 200

nofill()
stroke(.8)
path1 = oval(x + 40, y + 40, 80, 80, draw=True)
path2 = oval(x + 90, y + 40, 80, 80, draw=True)
compound = path1.xor(path2)
stroke(0)
fill(.8, .5)
drawpath(compound)

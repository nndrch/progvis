# ciclo de cores 

colormode(HSB)

x, y = 0, 0     # posição de origem
w = h = 12      # largura = altura (em módulos)
c = 13          # quantidade de cores
s = 40          # tamanho do módulo

# criar cores

_colors = []
for i in range(c):
    _color = color(random(), 1, 1)
    _colors.append(_color)

size(w*s, h*s)

_x, _y = x, y

_count = 0
for i in range(w):
    for j in range(h):
        _index = _count % c
        _color = _colors[_index]
        fill(_color)
        rect(_x, _y, s, s)
        _x += s
        _count += 1
    _x = x
    _y += s

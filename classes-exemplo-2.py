# objetos

class Page:

    color_pos = (1)
    color_neg = (0)

    def __init__(self, size, mode=0):
        self.mode = mode
        self.w, self.h = size

    def draw(self):
        size(self.w, self.h)
        if self.mode == 0:
            background(self.color_pos)
        else:
            background(self.color_neg)

class Logo():
    
    color_pos = (1, 0, 0)
    color_neg = (1, 1, 0)

    color_pos_txt = (0)
    color_neg_txt = (1)

    size = 13

    def __init__(self, page):
        self.page = page
        self._set_orientation()

    def _set_color(self):
        if self.page.mode == 0:
            fill(self.color_pos)
        else:
            fill(self.color_neg)

    def _set_orientation(self):
        if self.page.w > self.page.h:
            self.orientation = 1
        else:
            self.orientation = 0

    def _draw_logo(self, pos):
        x, y = pos
        if self.size < 30:
            oval(x, y, self.size, self.size)
        else:
            push()
            steps = 5
            for i in range(steps):
                rect(x, y, self.size, self.size)
                rotate(360/steps)
            pop()

    def _draw_text(self, pos):
        x, y = pos
        if self.page.mode == 0:
            fill(self.color_pos_txt)
        else:
            fill(self.color_neg_txt)
        font('Verdana', self.size)
        lineheight(1.0)
        if self.orientation == 1: # horizontal
            text('hello world', x + (self.size * 2), y + self.size)
        else: # vertical
            push()
            text('hello\nworld', x, y + (self.size * 3))
            pop()

    def draw(self, pos):
        self._set_color()
        self._draw_logo(pos)
        self._draw_text(pos)

# desenho

P = Page((628, 429))
P.mode = 1                  # 0: positivo / 1: negativo
P.draw()

L = Logo(P)
# L.orientation = 1         # 0: vertical / 1: horizontal
L.size = abs(53)
L.draw((90, 70))

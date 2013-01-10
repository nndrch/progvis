size(400, 300)

# http://nodebox.net/code/index.php/Variables

var('x', NUMBER, 30, 0, WIDTH)
var('y', NUMBER, 30, 0, HEIGHT)
var('text_', TEXT, default="hello")
var('color_', BOOLEAN)
var('do_something', BUTTON)

def do_something():
    print 'doing something'

if color_:
    fill(1, 0, 0)
else:
    fill(.5)

_text = '%s %s %s' % (text_, x, y)

font('Verdana', 16)
text(_text, x, y)

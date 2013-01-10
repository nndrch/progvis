# extraindo cores de uma imagem

# http://nodebox.net/code/index.php/Colors

colors = ximport('colors')

size(400, 600)

imagepath = u"/Users/gferreira0/Desktop/_fotos/Paraty/DSC01012.JPG"

image(imagepath, 0, 0, height=300)

_img_colors = colors.list(imagepath, n=20)

x, y = 0, HEIGHT/2

w = float(WIDTH) / len(_img_colors)

for c in _img_colors:
    fill(c)   
    rect(x, y, w, HEIGHT/2)
    x += w
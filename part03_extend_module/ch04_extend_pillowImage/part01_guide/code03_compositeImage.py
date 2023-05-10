from PIL import Image

im01 = Image.open('blend1.jpg')
#im01.show()
im02 = Image.open('blend2.jpg')
#im02.show()
im02 = im02.resize(im01.size)
r,g,b = im02.split()
Image.composite(im02,im01,b).show()


from PIL import Image
image = Image.open('bjsxt.png')
#image.show()
print('image format',image.format)
print('image size',image.size)
print('image height',image.height,'image width',image.width)
print('get the point(100,100)',image.getpixel((100,100)))


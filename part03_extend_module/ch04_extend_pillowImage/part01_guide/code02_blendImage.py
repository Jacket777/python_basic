from PIL import Image
#blend image
im01 = Image.open('bjsxt.png').convert('RGB')
im02 = Image.new("RGB",im01.size,"red")
#im02.show()
Image.blend(im01,im02,alpha=0.5).show()


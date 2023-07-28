from PIL import Image

img = Image.open('./tea1.png')
img.show()

box = (250, 250, 750, 750)
img2 = img.crop(box)

img2.save('C:\mystro6mystro6\python intermediat level\crop image\myimage_cropped2.jpg')
img2.show()

from PIL import Image

image = Image.open("pillow.png")
image = image.convert('L')

image.show()
image.save('gray-pillow.jpeg', 'jpeg')
from PIL import Image

img = Image.open('chat.jpg')

# Redimensionner l'image
resized_img = img.resize((100, 100))

# Recadrer une portion de l'image (x1, y1, x2, y2)
cropped_img = img.crop((50, 50, 200, 200))

resized_img.save('resized_chat.jpg')
cropped_img.save('cropped_chat.jpg')

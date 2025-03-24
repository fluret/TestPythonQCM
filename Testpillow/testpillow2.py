from PIL import Image, ImageDraw

# Créer une image blanche de taille 200x200 pixels
img = Image.new('RGB', (200, 200), color='white')
draw = ImageDraw.Draw(img)

# Dessiner un rectangle
draw.rectangle((50, 50, 150, 150), fill='blue')

img.save('output_image.png')

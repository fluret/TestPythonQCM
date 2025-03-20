from PIL import Image, ImageDraw, ImageFont

code = """def bonjour():
    print('Salut le monde !')"""

img = Image.new('RGB', (800, 400), color=(255, 255, 255))
d = ImageDraw.Draw(img)
font = ImageFont.load_default()  # Remplacez avec un chemin vers une vraie police si nécessaire
d.text((10, 10), code, fill=(0, 0, 0), font=font)
img.save("code_image.png")

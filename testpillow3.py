from PIL import Image
import base64
from io import BytesIO

# Ouvrir une image à l'aide de Pillow
img = Image.open("chat.jpg")

# Convertir l'image en un objet binaire (buffer en mémoire)
buffer = BytesIO()
img.save(buffer, format="JPEG")  # Spécifiez le format si nécessaire

# Encoder en Base64
encoded_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

# Afficher ou utiliser le résultat
print("Image encodée en Base64 :")
print(encoded_image)

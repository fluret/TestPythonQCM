import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
import base64
from PIL import Image

def process_folder(folder_path):
    # Crée un dossier pour les images si ce n'est pas déjà fait
    image_folder = os.path.join(folder_path, "images")
    os.makedirs(image_folder, exist_ok=True)

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                script_path = os.path.join(root, file)
                image_name = os.path.splitext(file)[0] + ".png"
                image_path = os.path.join(image_folder, image_name)

                # Convertit le script Python en image
                with open(script_path, "r") as script_file:
                    code = script_file.read()
                formatter = ImageFormatter()
                with open(image_path, "wb") as image_file:
                    highlight(code, PythonLexer(), formatter, image_file)

                # Encode l'image en Base64
                with open(image_path, "rb") as image_file:
                    image_data = image_file.read()
                base64_encoded = base64.b64encode(image_data).decode("utf-8")

                # Sauvegarde le contenu encodé dans un fichier texte
                base64_path = os.path.splitext(image_path)[0] + "_base64.txt"
                with open(base64_path, "w") as base64_file:
                    base64_file.write(base64_encoded)

                print(f"Script {file} traité : image et fichier Base64 générés.")

# Chemin du dossier à traiter (à personnaliser)
chemin_dossier = "./codes"
process_folder(chemin_dossier)

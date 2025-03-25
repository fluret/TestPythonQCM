import base64
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from io import BytesIO
import os
path = os.path.abspath(os.path.dirname(__file__))
import json
import re

def code_to_base64(code):
    """
    Convertit un code Python en une image encodée en Base64 sans stocker l'image sur le disque.
    
    :param code: Texte du code Python.
    :return: Chaîne encodée en Base64 représentant l'image du code.
    """
    # Crée un buffer en mémoire pour stocker l'image temporairement
    image_buffer = BytesIO()
    
    # Génère l'image du code Python
    formatter = ImageFormatter(line_numbers=False)
    highlight(code, PythonLexer(), formatter, image_buffer)
    
    # Encode l'image en Base64
    image_buffer.seek(0)  # Revenir au début du buffer
    image_data = image_buffer.read()
    base64_encoded = base64.b64encode(image_data).decode("utf-8")
    
    # Ferme le buffer
    image_buffer.close()
    
    return base64_encoded


def transformer_questions(fichier_json, fonction_base64):
    """
    Transforme le contenu de 'text' dans un fichier JSON en remplaçant les balises <pre><code> et </code></pre>.
    
    :param fichier_json: Chemin du fichier JSON à modifier.
    :param fonction_base64: Fonction qui génère une chaîne Base64 à partir d'un texte.
    """
    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)

    def parcourir_questions(questions):
        for question in questions:
            if "text" in question:
                # Séparer la partie avant les balises (A) et le contenu entre les balises (B)
                match = re.search(r'(.*)<pre><code>(.*?)</code></pre>', question["text"], re.DOTALL)
                if match:
                    partie_a = match.group(1).strip()
                    partie_b = match.group(2).strip()
                    
                    # Générer le contenu Base64 pour la partie B
                    base64_image = fonction_base64(partie_b)
                    
                    # Remplacer le contenu de "text"
                    question["text"] = f'<![CDATA[ {partie_a} <img src="@@PLUGINFILE@@/args001.png" alt="" role="presentation">]]></text><file name="args001.png" path="/" encoding="base64">{base64_image}</file>'
            
            if "questions" in question:  # Si des sous-questions existent
                parcourir_questions(question["questions"])

    parcourir_questions(data)
    # Sauvegarder les modifications dans le fichier JSON
    with open(fichier_json, 'w', encoding='utf-8') as fichier:
        json.dump(data, fichier, ensure_ascii=False, indent=4)
        
# Exemple d'utilisation
def convert_base64(code):
    """
    Exemple de fonction qui génère une chaîne Base64 à partir d'un texte.
    Remplacez cette fonction par votre implémentation réelle.
    """
    import base64
    return base64.b64encode(code.encode('utf-8')).decode('utf-8')


fichier = f"{path}\\questions.json"  # Remplacez par le chemin réel de votre fichier
transformer_questions(fichier, convert_base64)
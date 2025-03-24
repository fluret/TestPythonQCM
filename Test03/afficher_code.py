import json
import re
import os
path = os.path.abspath(os.path.dirname(__file__))




def extraire_code_json(fichier_json):
    """
    Extrait le contenu entre les balises <pre><code> et </code></pre> dans un fichier JSON.
    
    :param fichier_json: Chemin du fichier JSON à traiter.
    :return: Liste des extraits de code trouvés.
    """
    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)
    
    codes = []
    
    def parcourir_questions(questions):
        for question in questions:
            if "text" in question:
                # Recherche du contenu entre <pre><code> et </code></pre>
                matches = re.findall(r'<pre><code>(.*?)</code></pre>', question["text"], re.DOTALL)
                codes.extend(matches)
            if "questions" in question:  # Si des sous-questions existent
                parcourir_questions(question["questions"])
    
    parcourir_questions(data)
    return codes

# Exemple d'utilisation
fichier = f"{path}\\questions.json"  # Remplacez par le chemin réel de votre fichier
extraits = extraire_code_json(fichier)
for extrait in extraits:
    print(extrait)
from lxml import etree
import os

# Obtenir le chemin absolu du fichier
path = os.path.abspath(os.path.dirname(__file__))

# Charger le fichier XML
tree = etree.parse(f"{path}\\sample.xml")

# Parcourir les balises <question> dans le fichier XML
for category in tree.xpath("/quiz/question"):
    print(f"Type de question : {category.get('type')}")
    
    # Vérifier si le type est "multichoice"
    if category.get("type") == "multichoice":
        # Extraire la balise <name>
        nom = category.xpath("name/text")
        if nom:  # Vérifier si la balise <text> existe dans <name>
            print(f"Nom de la question : {nom[0].text}")
        else:
            print("La balise <text> dans <name> est absente.")
        texte_question = category.xpath("questiontext/text")
        if texte_question:
            print(f"Texte de la question : {texte_question[0].text}")
        for answer in category.xpath("answer"):
            texte_reponse = answer.xpath("text")
            if texte_reponse:
                print(f"Texte de la réponse : {texte_reponse[0].text}")
            else:
                print("La balise <text> dans <answer> est absente.")
            format_value = answer.get("format", "Non spécifié")
            fraction_value = answer.get("fraction", "Non spécifié")
            print(f"Attribut format : {format_value}")
            print(f"Attribut fraction : {fraction_value} c'est la {"bonne réponse" if int(fraction_value) >= 0 else "mauvaise réponse"}")
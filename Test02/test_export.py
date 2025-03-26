import json
import xml.etree.ElementTree as ET
import os

# Définir le chemin du répertoire courant
path = os.path.abspath(os.path.dirname(__file__))

def create_moodle_xml(json_filepath, xml_filepath):
    """
    Génère un fichier XML Moodle à partir d'un fichier JSON contenant des catégories et des questions.
    """
    try:
        # Charger les données JSON
        with open(json_filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Créer l'élément racine pour le XML
        root = ET.Element("quiz")

        for category_data in data:
            # Vérifier si la catégorie existe
            category_name = category_data.get("category", "Default Category")
            if not category_name:
                print("Catégorie manquante, elle sera ignorée.")
                continue

            # Ajouter une catégorie
            category_element = ET.SubElement(root, "question", {"type": "category"})
            category_text = ET.SubElement(ET.SubElement(category_element, "category"), "text")
            category_text.text = category_name

            # Ajouter les questions de la catégorie
            for question_data in category_data.get("questions", []):
                question_type = question_data.get("type", "unknown")
                question_text = question_data.get("text", "Unnamed Question")

                # Ajouter une question
                question_element = ET.SubElement(root, "question", {"type": question_type})

                # Ajouter le nom de la question
                name_element = ET.SubElement(question_element, "name")
                name_text = ET.SubElement(name_element, "text")
                name_text.text = question_text

                # Ajouter les réponses si elles existent
                for answer in question_data.get("answers", []):
                    fraction = str(answer.get("fraction", 0))
                    answer_text_value = answer.get("text", "")

                    # Ajouter une réponse
                    answer_element = ET.SubElement(question_element, "answer", {"fraction": fraction})
                    answer_text = ET.SubElement(answer_element, "text")
                    answer_text.text = answer_text_value

        # Écrire le fichier XML
        tree = ET.ElementTree(root)
        tree.write(xml_filepath, encoding="utf-8", xml_declaration=True)
        print(f"Fichier XML Moodle généré : {xml_filepath}")

    except json.JSONDecodeError as e:
        print(f"Erreur lors du chargement du fichier JSON : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    json_filepath = f"{path}\\questions.json"  # Chemin du fichier JSON
    xml_filepath = f"{path}\\new_moodle.xml"  # Chemin du fichier XML de sortie
    create_moodle_xml(json_filepath, xml_filepath)
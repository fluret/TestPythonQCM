import json
from lxml import etree
import os

path = os.path.abspath(os.path.dirname(__file__))


def json_to_moodle_xml(json_filepath, xml_filepath):
    """
    Convertit un fichier JSON contenant des catégories et des questions en un fichier XML Moodle.
    """
    try:
        # Charger les données JSON
        with open(json_filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Créer l'élément racine pour le XML
        root = etree.Element("quiz")

        for category_data in data:
            # Ajouter une catégorie
            category_element = etree.SubElement(root, "question", {"type": "category"})
            category_text = etree.SubElement(etree.SubElement(category_element, "category"), "text")
            category_text.text = category_data.get("category", "Unnamed Category")

            # Ajouter les questions de la catégorie
            for question_data in category_data.get("questions", []):
                question_type = question_data.get("type", "unknown")
                question_text = question_data.get("text", "Unnamed Question")

                # Ajouter une question
                question_element = etree.SubElement(root, "question", {"type": question_type})
                #ajouter le nom de la question
                name_element = etree.SubElement(question_element, "name")
                name_text = etree.SubElement(name_element, "text")
                name_text.text = question_data.get("name", "Unnamed Question")
                # Ajouter le texte de la question
                questiontext_element = etree.SubElement(question_element, "questiontext", {"format": "html"})
                questiontext_text = etree.SubElement(questiontext_element, "text")

                # Ajouter le texte HTML tel quel (avec CDATA)
                questiontext_text.text = etree.CDATA(question_text)

                # Ajouter les réponses si elles existent
                for answer in question_data.get("answers", []):
                    # Convertir fraction en chaîne
                    fraction = str(answer.get("fraction", 0))
                    # Convertir le texte de la réponse en chaîne (si c'est un booléen)
                    answer_text_value = str(answer.get("text", ""))

                    # Ajouter une réponse
                    answer_element = etree.SubElement(question_element, "answer", {"fraction": fraction})
                    answer_text = etree.SubElement(answer_element, "text")
                    answer_text.text = answer_text_value

                # Ajouter les sous-questions pour les questions de type "matching"
                if question_type == "matching":
                    for sub_question in question_data.get("matching_pairs", []):
                        subquestion_element = etree.SubElement(question_element, "subquestion")
                        subquestion_text = etree.SubElement(subquestion_element, "text")
                        subquestion_text.text = str(sub_question.get("text", ""))
                        answer_element = etree.SubElement(subquestion_element, "answer")
                        answer_text = etree.SubElement(answer_element, "text")
                        answer_text.text = str(sub_question.get("answer", ""))

        # Écrire le fichier XML
        tree = etree.ElementTree(root)
        tree.write(xml_filepath, encoding="utf-8", pretty_print=True, xml_declaration=True)
        print(f"Fichier XML Moodle généré : {xml_filepath}")

    except json.JSONDecodeError as e:
        print(f"Erreur lors du chargement du fichier JSON : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


# Exemple d'utilisation
if __name__ == "__main__":
    json_filepath = f"{path}\\questions.json"  # Chemin du fichier JSON
    xml_filepath = f"{path}\\new_moodle.xml"  # Chemin du fichier XML de sortie
    json_to_moodle_xml(json_filepath, xml_filepath)
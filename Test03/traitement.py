#from questions import Question
#from category import Category
from moodlexmlparser import MoodleXMLParser
from gestjson import export_questions_to_json, load_questions_from_json
import os
path = os.path.abspath(os.path.dirname(__file__))


input_filepath = f"{path}\\quiz03.xml"  # Chemin vers le fichier XML Moodle
output_filepath = f"{path}\\questions.json"  # Chemin vers le fichier JSON de sortie

# Analyse du fichier XML
parser = MoodleXMLParser(input_filepath)
parser.parse()

# Exportation en JSON
export_questions_to_json(parser, output_filepath)

# Chargement depuis le fichier JSON et affichage des données
questions_data = load_questions_from_json(output_filepath)
for category in questions_data:
    print(f"Catégorie : {category['category']}")
    for question in category["questions"]:
        print(f"  Question ({question['type']}) : {question['text']}")
        if question["answers"]:
            for answer in question["answers"]:
                correct = "(Correct)" if answer["fraction"] > 0 else ""
                print(f"    - {answer['text']} {correct}")
        if question["matching_pairs"]:
            for pair in question["matching_pairs"]:
                print(f"    - {pair['question']} -> {pair['answer']} (Matching)")

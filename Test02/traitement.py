import json
import xml.etree.ElementTree as ET
import os
path = os.path.abspath(os.path.dirname(__file__))

# Classes existantes
class Question:
    def __init__(self, text, qtype):
        self.text = text
        self.qtype = qtype
        self.answers = []
        self.matching_pairs = []

    def add_multichoice_answer(self, text, fraction):
        self.answers.append({"text": text, "fraction": fraction})

    def set_truefalse_answer(self, text):
        self.answers.append({"text": text, "fraction": 100 if text else 0})

    def set_shortanswer_answer(self, text):
        self.answers.append({"text": text, "fraction": 100})

    def add_matching_pair(self, question, answer):
        self.matching_pairs.append({"question": question, "answer": answer})

class Category:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

class MoodleXMLParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.categories = []

    def parse(self):
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        self.categories = self._extract_categories(root)

    def _extract_categories(self, root):
        categories = []
        current_category = None

        for question in root.findall("question"):
            qtype = question.get("type")

            if qtype == "category":
                category_text_element = question.find("category").find("text")
                category_name = category_text_element.text if category_text_element is not None else "Unnamed Category"
                current_category = Category(category_name)
                categories.append(current_category)

            elif current_category and qtype in {"multichoice", "truefalse", "shortanswer", "matching"}:
                question_text = question.find("questiontext").find("text").text
                new_question = self._extract_question_details(question, qtype, question_text)
                current_category.add_question(new_question)

        return categories

    def _extract_question_details(self, question, qtype, question_text):
        new_question = Question(question_text, qtype)

        if qtype == "multichoice":
            for answer in question.findall("answer"):
                answer_text = answer.find("text").text
                fraction = int(answer.get("fraction", 0))
                new_question.add_multichoice_answer(answer_text, fraction)

        elif qtype == "truefalse":
            for answer in question.findall("answer"):
                answer_text = answer.find("text").text.lower() == "true"
                fraction = int(answer.get("fraction", 0))
                new_question.set_truefalse_answer(answer_text)

        elif qtype == "shortanswer":
            for answer in question.findall("answer"):
                answer_text = answer.find("text").text
                new_question.set_shortanswer_answer(answer_text)

        elif qtype == "matching":
            for sub_question in question.findall("subquestion"):
                sub_question_text = sub_question.find("text").text
                answer_text = sub_question.find("answer").find("text").text
                new_question.add_matching_pair(sub_question_text, answer_text)

        return new_question

# Exportation en JSON
def export_questions_to_json(parser, output_filepath):
    all_data = []

    for category in parser.categories:
        category_data = {
            "category": category.name,
            "questions": []
        }

        for question in category.questions:
            question_data = {
                "text": question.text,
                "type": question.qtype,
                "answers": [],
                "matching_pairs": []
            }

            if question.qtype in {"multichoice", "truefalse", "shortanswer"}:
                for answer in question.answers:
                    question_data["answers"].append({
                        "text": answer["text"],
                        "fraction": answer["fraction"]
                    })

            if question.qtype == "matching":
                for pair in question.matching_pairs:
                    question_data["matching_pairs"].append({
                        "question": pair["question"],
                        "answer": pair["answer"]
                    })

            category_data["questions"].append(question_data)

        all_data.append(category_data)

    with open(output_filepath, "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)
    print(f"Questions exportées dans le fichier : {output_filepath}")

# Lecture du JSON généré
def load_questions_from_json(filepath):
    with open(filepath, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

# Exemple d'utilisation
if __name__ == "__main__":
    input_filepath = f"{path}\\quiz02.xml"  # Chemin vers le fichier XML Moodle
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

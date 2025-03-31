import xml.etree.ElementTree as ET
from category import Category
from questions import Question

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
            question_name = question.find("name").find("text").text if question.find("name") is not None else "Unnamed Question"
            if qtype == "category":
                category_text_element = question.find("category").find("text")
                category_name = category_text_element.text if category_text_element is not None else "Unnamed Category"
                current_category = Category(category_name)
                categories.append(current_category)

            elif current_category and qtype in {"multichoice", "truefalse", "shortanswer", "matching"}:
                question_text = question.find("questiontext").find("text").text
                new_question = self._extract_question_details(question, qtype, question_text, question_name)
                current_category.add_question(new_question)

        return categories

    def _extract_question_details(self, question, qtype, question_text, name):
        new_question = Question(question_text, qtype, name)

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
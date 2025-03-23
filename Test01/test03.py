import unittest

# Importez ici les classes Category, Question et MoodleXMLParser
from category import Category
from questions import Question
from moodlexmlparser import MoodleXMLParser
import os
path = os.path.abspath(os.path.dirname(__file__))


class TestMoodleXMLImport(unittest.TestCase):
    def setUp(self):
        # Chemin vers le fichier XML Moodle
        self.filepath = "quiz.xml"
        self.parser = MoodleXMLParser(path + "\\" + self.filepath)
    
    def test_import_questions(self):
        # Analyse du fichier XML
        self.parser.parse()
        categories = self.parser.categories

        # Vérifie que des catégories ont été importées
        self.assertGreater(len(categories), 0, "Aucune catégorie importée depuis le fichier XML.")

        # Vérifie la première catégorie et ses questions
        first_category = categories[0]
        self.assertIsInstance(first_category, Category, "La première catégorie n'est pas du bon type.")
        self.assertGreater(len(first_category.questions), 0, "Aucune question dans la première catégorie.")

        # Vérifie les questions
        for question in first_category.questions:
            self.assertIsInstance(question, Question, "Une question n'est pas du bon type.")
            self.assertIn(question.qtype, {"multichoice", "truefalse", "shortanswer", "matching"},
                          "Type de question inconnu.")

        # Vérifie une question spécifique
        question = first_category.questions[0]
        if question.qtype == "multichoice":
            self.assertEqual(question.text, "What is the capital of France?")
            self.assertEqual(len(question.answers), 3)
            self.assertEqual(question.answers[0]["text"], "Paris")
            self.assertEqual(question.answers[0]["fraction"], 100)

        if question.qtype == "truefalse":
            self.assertEqual(question.text, "Python is a programming language.")
            self.assertEqual(len(question.answers), 2)
            self.assertEqual(question.answers[0]["text"], "True")
            self.assertEqual(question.answers[0]["fraction"], 100)

if __name__ == "__main__":
    unittest.main()

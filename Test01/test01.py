from quizmanager import QuizManager
from category import Category
from questions import Question

manager = QuizManager()

# Charger un fichier existant
manager.load_from_file("quiz.xml")

# Ajouter une catégorie et une question
new_category = Category("New Category")
new_question = Question("What is Python?")
new_question.add_answer("A programming language", 100)
new_question.add_answer("A snake", 0)
new_category.add_question(new_question)
manager.add_category(new_category)

# Sauvegarder les modifications dans un fichier
manager.save_to_file("new_quiz.xml")

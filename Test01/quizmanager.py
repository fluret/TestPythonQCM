from category import Category
from moodlexmlparser import MoodleXMLParser
from moodlexmlwriter import MoodleXMLWriter


class QuizManager:
    def __init__(self):
        self.categories = []

    def load_from_file(self, filepath: str):
        parser = MoodleXMLParser(filepath)
        parser.parse()
        self.categories = parser.categories
    
    def save_to_file(self, filepath: str):
        writer = MoodleXMLWriter(self.categories)
        writer.write(filepath)
    
    def add_category(self, category: Category):
        self.categories.append(category)

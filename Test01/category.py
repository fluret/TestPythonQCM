class Category:
    def __init__(self, name: str):
        self.name = name
        self.questions = []
    
    def add_question(self, question):
        self.questions.append(question)

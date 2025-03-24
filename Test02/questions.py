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
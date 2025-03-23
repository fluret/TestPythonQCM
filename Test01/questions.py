class Question:
    def __init__(self, text: str, qtype: str):
        """
        Initialise une question Moodle.

        :param text: Le texte de la question.
        :param qtype: Le type de la question (multichoice, truefalse, shortanswer, matching).
        """
        if qtype not in {"multichoice", "truefalse", "shortanswer", "matching"}:
            raise ValueError(f"Type de question non pris en charge : {qtype}")
        
        self.text = text
        self.qtype = qtype
        self.answers = []  # Liste pour stocker les réponses
        self.matching_pairs = []  # Utilisé uniquement pour les questions de type "matching"

    def add_multichoice_answer(self, answer_text: str, fraction: int):
        """
        Ajoute une réponse pour une question à choix multiple.

        :param answer_text: Texte de la réponse.
        :param fraction: Pourcentage de la note (100 pour la bonne réponse, 0 pour une mauvaise).
        """
        if self.qtype != "multichoice":
            raise TypeError("Cette méthode est uniquement pour les questions à choix multiple.")
        self.answers.append({"text": answer_text, "fraction": fraction})

    def set_truefalse_answer(self, is_true: bool):
        """
        Définit la réponse correcte pour une question vrai/faux.

        :param is_true: True si la bonne réponse est "vrai", False sinon.
        """
        if self.qtype != "truefalse":
            raise TypeError("Cette méthode est uniquement pour les questions vrai/faux.")
        self.answers = [{"text": "True", "fraction": 100 if is_true else 0},
                        {"text": "False", "fraction": 100 if not is_true else 0}]

    def set_shortanswer_answer(self, answer_text: str):
        """
        Définit la réponse correcte pour une question à réponse courte.

        :param answer_text: La réponse correcte.
        """
        if self.qtype != "shortanswer":
            raise TypeError("Cette méthode est uniquement pour les questions à réponse courte.")
        self.answers.append({"text": answer_text, "fraction": 100})

    def add_matching_pair(self, question_text: str, answer_text: str):
        """
        Ajoute une paire question-réponse pour une question de type "matching".

        :param question_text: Texte de la sous-question.
        :param answer_text: Texte de la réponse correspondante.
        """
        if self.qtype != "matching":
            raise TypeError("Cette méthode est uniquement pour les questions de type matching.")
        self.matching_pairs.append({"question": question_text, "answer": answer_text})

    def __str__(self):
        """
        Retourne une représentation textuelle de la question.
        """
        if self.qtype == "matching":
            matching_str = "\n".join([f"{pair['question']} -> {pair['answer']}" for pair in self.matching_pairs])
            return f"Question (Matching): {self.text}\nPairs:\n{matching_str}"
        else:
            answers_str = "\n".join([f"{ans['text']} (fraction: {ans['fraction']})" for ans in self.answers])
            return f"Question ({self.qtype}): {self.text}\nAnswers:\n{answers_str}"

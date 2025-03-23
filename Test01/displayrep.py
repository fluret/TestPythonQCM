from moodlexmlparser import MoodleXMLParser
import os
path = os.path.abspath(os.path.dirname(__file__))


def display_questions(parser):
    """
    Affiche les questions et les réponses avec indication de la bonne réponse.

    :param parser: Instance de MoodleXMLParser ayant déjà analysé le fichier XML.
    """
    for category in parser.categories:
        print(f"Catégorie : {category.name}")
        print("-" * 50)
        for question in category.questions:
            print(f"Question ({question.qtype}): {question.text}")
            
            if question.qtype == "multichoice":
                for answer in question.answers:
                    correct = "(Correct)" if answer["fraction"] > 0 else ""
                    print(f"- {answer['text']} {correct}")
            
            elif question.qtype == "truefalse":
                for answer in question.answers:
                    correct = "(Correct)" if answer["fraction"] > 0 else ""
                    print(f"- {answer['text']} {correct}")
            
            elif question.qtype == "shortanswer":
                for answer in question.answers:
                    print(f"- {answer['text']} (Correct)")
            
            elif question.qtype == "matching":
                print("Matching pairs:")
                for pair in question.matching_pairs:
                    print(f"- {pair['question']} -> {pair['answer']} (Correct)")
            
            print("\n")
        print("=" * 50)

# Exemple d'utilisation
if __name__ == "__main__":
    filepath = "quiz02.xml"  # Chemin vers votre fichier XML Moodle
    parser = MoodleXMLParser(path + "\\" + filepath)
    parser.parse()
    display_questions(parser)

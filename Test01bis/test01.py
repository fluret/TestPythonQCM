'''
Ouverture du fichier XML, parcours de l'arbre XML et affichage des catégories
'''

from lxml import etree
import os

path = os.path.abspath(os.path.dirname(__file__))
file = path + "\\celeneargs_11Q.xml"

tree = etree.parse(file)
root = tree.getroot()
#print(etree.tostring(root, pretty_print=True).decode())
print('*'*20)
for question in root.findall("question"):
    qtype = question.get("type")
    if qtype == "category":
        # Récupérer le nom de la catégorie
        category_text_element = question.find("category").find("text")
        category_name = category_text_element.text if category_text_element.text else "Unnamed Category"
        print(f'Category: {category_name} et {category_name}')
print('*'*20)
for question in root.findall("question"):
    qtype = question.get("type")
    if qtype == "category":
        # Récupérer le nom de la catégorie
        category_text_element = question.find("category").find("text")
        category_name = category_text_element.text if category_text_element.text else "Unnamed Category"
        print(f'Category: {category_name} et {category_name}')
    elif qtype in {"multichoice", "truefalse", "shortanswer", "matching"}:
        # Récupérer le texte de la balise <name>
        name_element = question.find("name")
        name_text = name_element.find("text").text if name_element is not None else "Unnamed Question"
        
        # Récupérer le texte de la question
        question_text_element = question.find("questiontext").find("text")
        question_text = question_text_element.text if question_text_element is not None else "No Question Text"
        
        print(f'\tQuestion Name: {name_text}')
        print(f'\tQuestion Text:\n {question_text}')
        print('-'*10)
#afficher le nombre d'intitulé "question"

path = os.path.abspath(os.path.dirname(__file__))
file = path + "\\celeneargs_testnbq.xml"

tree = etree.parse(file)
root = tree.getroot()

print(len(root.findall("question")))

count_between_categories = 0
inside_category_block = False

for question in root.findall("question"):
    qtype = question.get("type")

    if qtype == "category":
        # Si on rencontre une nouvelle catégorie, afficher le compteur précédent
        if inside_category_block:
            print(f"Nombre de questions entre deux catégories : {count_between_categories}")
            count_between_categories = 0  # Réinitialiser le compteur
        inside_category_block = True  # On est dans un bloc de catégorie
    elif inside_category_block:
        # Compter les questions dont le type est différent de "category"
        count_between_categories += 1

# Afficher le dernier compteur si nécessaire
if inside_category_block:
    print(f"Nombre de questions entre deux catégories : {count_between_categories}")
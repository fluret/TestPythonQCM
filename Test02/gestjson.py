import json
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
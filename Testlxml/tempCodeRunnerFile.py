for question in category.xpath("questiontext/text"):
            print(question.text)
            
        for answer in category.xpath("answer/text"):
            print(answer.text)
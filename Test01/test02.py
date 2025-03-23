from questions import Question

# Question multichoice
q1 = Question("What is the capital of France?", "multichoice")
q1.add_multichoice_answer("Paris", 100)
q1.add_multichoice_answer("London", 0)
q1.add_multichoice_answer("Berlin", 0)
print(q1)

# Question true/false
q2 = Question("Python is a programming language.", "truefalse")
q2.set_truefalse_answer(True)
print(q2)

# Question shortanswer
q3 = Question("What is 2 + 2?", "shortanswer")
q3.set_shortanswer_answer("4")
print(q3)

# Question matching
q4 = Question("Match the countries to their capitals.", "matching")
q4.add_matching_pair("France", "Paris")
q4.add_matching_pair("Germany", "Berlin")
q4.add_matching_pair("Italy", "Rome")
print(q4)

def fonction_travail(*args):
    for index, arg in enumerate(reversed(args)):
        print(f": {arg}")

fonction_travail(10, 20, 30)
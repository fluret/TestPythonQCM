def fonction_travail(*args):
    for index, arg in enumerate(reversed(args), start=1):
        print(f"{index}: {arg}")


fonction_travail(10, 20, 30)
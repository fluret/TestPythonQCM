def fonction_travail(**kwargs):
    print(kwargs.get("z", 100))

fonction_travail(x=10, y=20)
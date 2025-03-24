def fonction_travail(**kwargs):
    for value, key in kwargs.items():
        print(f"{value}: {key}")

fonction_travail(a=1, b=2)
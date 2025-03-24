def fonction_travail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

fonction_travail(a=1, b=2)
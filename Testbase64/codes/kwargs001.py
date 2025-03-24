def fonction_travail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

fonction_travail(nom="Alice", age=25)
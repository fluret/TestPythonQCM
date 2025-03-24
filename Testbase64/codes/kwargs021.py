def fonction_travail(**kwargs):
    for index, (key, value) in enumerate(kwargs.items(), start=1):
        print(f"{index}: {value}: {key}")

fonction_travail(a=1, b=2)
def fonction_travail(**kwargs):
    for index, (key, value) in enumerate(kwargs.items(), start=1):
        print(f"{index}: {key}: {value}")

fonction_travail(a=1, b=2)
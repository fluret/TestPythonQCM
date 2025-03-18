def fonction_travail(**kwargs):
    base = {"a": 1, "b": 2}
    return {**base, **kwargs}

result = fonction_travail(b=3, c=4)

print(result)
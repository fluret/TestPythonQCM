def fonction_travail(**kwargs):
    return kwargs

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

resultat = fonction_travail(**d1, **d2)
print(resultat)
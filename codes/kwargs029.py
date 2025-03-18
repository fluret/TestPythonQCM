def fonction_travail(**kwargs):
    kwargs["x"] = 50
    return kwargs

resultat = fonction_travail(x=10, y=20)
print(resultat)
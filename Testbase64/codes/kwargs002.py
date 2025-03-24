def fonction_travail(**kwargs):
    del(kwargs["x"])
    return kwargs

resultat = fonction_travail(x=10, y=20)
print(resultat)
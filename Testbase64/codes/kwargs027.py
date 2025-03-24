def fonction_travail(**kwargs):
    kwargs["nouveau"] = 100
    return kwargs

resultat = fonction_travail(a=1, b=2)
print(resultat)
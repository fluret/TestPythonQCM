def fonction_travail(x):
    return x == 60

result = list(filter(fonction_travail, [60, 120, 180, 240]))
print(result)
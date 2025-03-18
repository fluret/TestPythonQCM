def fonction_travail(x):
    return x < 70

result = list(filter(fonction_travail, [50, 60, 70, 80]))
print(result)
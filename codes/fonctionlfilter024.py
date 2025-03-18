def fonction_travail(x):
    return x < 50

result = list(filter(fonction_travail, [30, 40, 50, 60]))
print(result)
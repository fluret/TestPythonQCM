def fonction_travail(x):
    return x == 50

result = list(filter(fonction_travail, [50, 100, 150, 200]))
print(result)
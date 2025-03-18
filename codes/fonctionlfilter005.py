def fonction_travail(x):
    return x < 0

result = list(filter(fonction_travail, [-1, -2, 0, 1, 2]))
print(result)
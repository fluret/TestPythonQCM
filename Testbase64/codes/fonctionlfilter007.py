def fonction_travail(x):
    return x == 0

result = list(filter(fonction_travail, [0, 1, 2, 3, 0]))
print(result)
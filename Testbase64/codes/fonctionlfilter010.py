def fonction_travail(x):
    return x == 1

result = list(filter(fonction_travail, [1, 0, 1, 2, 3]))
print(result)
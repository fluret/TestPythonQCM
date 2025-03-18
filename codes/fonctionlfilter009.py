def fonction_travail(x):
    return x < 5

result = list(filter(fonction_travail, [1, 2, 3, 4, 5]))
print(result)
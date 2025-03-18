def fonction_travail(x):
    return x % 2 == 0

result = list(filter(fonction_travail, [1, 2, 3, 4]))
print(result)
def fonction_travail(x):
    return x % 3 == 0

result = list(filter(fonction_travail, [1, 2, 3, 4, 5, 6]))
print(result)
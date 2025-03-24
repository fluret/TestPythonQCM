def fonction_travail(x):
    return x != 10

result = list(filter(fonction_travail, [10, 20, 30, 40]))
print(result)
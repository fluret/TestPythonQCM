def fonction_travail(x):
    return x != 5

result = list(filter(fonction_travail, [5, 10, 15, 20, 25]))
print(result)
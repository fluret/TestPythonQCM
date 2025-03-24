def fonction_travail(x):
    return x == 20

result = list(filter(fonction_travail, [20, 40, 60, 80]))
print(result)
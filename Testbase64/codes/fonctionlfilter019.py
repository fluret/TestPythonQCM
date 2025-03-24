def fonction_travail(x):
    return x == 3

result = list(filter(fonction_travail, [3, 6, 9, 12]))
print(result)
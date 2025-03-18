def fonction_travail(x):
    return x > 10

result = filter(fonction_travail, [5, 15, 25, 35])
print(list(result))
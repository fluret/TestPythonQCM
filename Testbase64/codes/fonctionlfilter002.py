def fonction_travail(x):
    return x > 0

result = filter(fonction_travail, [-1, 0, 1, 2])
print(list(result))
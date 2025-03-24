def fonction_travail(x):
    return x > 30

result = filter(fonction_travail, [20, 30, 40, 50])
print(list(result))
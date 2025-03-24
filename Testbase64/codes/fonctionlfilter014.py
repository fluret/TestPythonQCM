def fonction_travail(x):
    return x > 20

result = filter(fonction_travail, [10, 20, 30, 40])
print(list(result))
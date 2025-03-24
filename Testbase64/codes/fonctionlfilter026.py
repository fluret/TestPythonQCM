def fonction_travail(x):
    return x > 40

result = filter(fonction_travail, [30, 40, 50, 60])
print(list(result))
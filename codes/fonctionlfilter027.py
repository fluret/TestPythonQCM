def fonction_travail(x):
    return x < 60

result = list(filter(fonction_travail, [40, 50, 60, 70]))
print(result)
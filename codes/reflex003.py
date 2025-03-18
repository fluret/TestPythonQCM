def fonction_travail(*args):
    return list(zip(*args))

print(fonction_travail([1,2,3], [4,5,6]))
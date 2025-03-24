def fonction_travail(**kwargs):
    result = []
    for v in kwargs.values():
        if isinstance(v, list):
            result += v
    return result

print(fonction_travail(a=[1, 2], b="hello", c=[3, 4]))
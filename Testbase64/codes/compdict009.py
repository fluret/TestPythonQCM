original = {'a': 1, 'b': 2, 'c': 3}
d = {value: key for key, value in original.items()}
print(d)
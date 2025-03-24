result = list(map(lambda x: x % 2, [1, 2, 3, 4, 5]))
print(result)  # [1, 0, 1, 0, 1]

def fct(x):
    return x % 2

result = list(map(fct, [1, 2, 3, 4, 5]))

print(result)  # [1, 0, 1, 0, 1]

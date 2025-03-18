result = list(map(lambda x: len(x), ['apple', 'banana', 'cherry']))
print(result)  # [5, 6, 6]

def fct(x):
    return len(x)

result = list(map(fct, ['apple', 'banana', 'cherry']))

print(result)


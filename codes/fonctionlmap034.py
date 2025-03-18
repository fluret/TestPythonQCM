
result = list(map(lambda x: x.upper(), ['a', 'b', 'c']))
print(result)  # ['A', 'B', 'C']

def fct(x):
    return x.upper()

result = list(map(fct, ['a', 'b', 'c']))

print(result)

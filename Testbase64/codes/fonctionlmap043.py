result = list(map(lambda x: x + '!', ['hello', 'world']))
print(result)  # ['hello!', 'world!']


def fct(x):
    return x + '!'
result = list(map(fct, ['hello', 'world']))
print(result)  # ['hello!', 'world!']
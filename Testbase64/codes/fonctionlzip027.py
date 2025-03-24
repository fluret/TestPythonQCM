letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for i, (letter, number) in enumerate(zip(letters, numbers)):
    print(f"{i}: {letter}-{number}")
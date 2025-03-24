n = 10
fibonacci = [0, 1]
[fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) for i in range(2, n)]
print(fibonacci)


n = 10
fibonacci = [0, 1] + [fibonacci[i - 1] + fibonacci[i - 2] for i in range(2, n)]
print(fibonacci)
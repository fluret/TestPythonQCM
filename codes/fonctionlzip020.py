result = list(zip([1, 2], ['a', 'b'], [True, False], [10, 20], [100, 200], [1000, 2000], strict=True))
print(result)  # [(1, 'a', True, 10, 100, 1000), (2, 'b', False, 20, 200, 2000)]
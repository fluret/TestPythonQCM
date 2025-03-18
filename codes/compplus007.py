lst = ["a", "b", "c", "d"]
result = [
    (index, char)
    for index, char in enumerate(lst)
    if index % 2 == 0 or char in ["b", "d"]
]

print(result)
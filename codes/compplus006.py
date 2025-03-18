lst = [1, 2, 2, 3, 4, 1, 5, 5, 3]
d = {item: lst.count(item) for item in set(lst)}
print(d)
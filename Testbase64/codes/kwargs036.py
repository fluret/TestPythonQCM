d1 = {"a": 1}
d2 = {"b": 2}
def merge(d1, d2):
    return {**d1, **d2}

def merge_2(d1, d2):
    d1.update(d2)
    return d1

def merge_3(d1, d2):
    return dict(d1, **d2)


print(merge(d1, d2))
print(merge_2(d1, d2))
print(merge_3(d1, d2))
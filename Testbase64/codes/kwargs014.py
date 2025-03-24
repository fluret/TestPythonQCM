def update_dict(base, **kwargs):
    return {**base, **kwargs}

base = {"a": 1, "b": 2}
result = update_dict(base, a=3, c=4)
print(result)
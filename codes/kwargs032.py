def fonction_travail(**kwargs):
    result = {}
    for k, v in kwargs.items():
        if isinstance(v, dict):
            result = {**result, **v}
    return result

print(fonction_travail(d1={"a": 1}, d2={"b": 2}, x=42,d3={"b": 3}, d4={"c": 4}))
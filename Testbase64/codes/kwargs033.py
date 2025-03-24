def fonction_travail(**kwargs):
    type_map = {"name": (str,'str'), "age": (int,'int')}
    for k, v in kwargs.items():
        if k in type_map and not isinstance(v, type_map[k][0]):
            print(f"{k} must be of type {type_map[k][1]}")
        
fonction_travail(name="Bob", age="25")

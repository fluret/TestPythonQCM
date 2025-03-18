def fonction_travail(**kwargs):
    required = {"name", "age"}
    missing = required - set(kwargs.keys())
    if missing:
        print(f"Missing keys: {missing}")
        
fonction_travail(name="Alice", age=25)
fonction_travail(name="Bob")
fonction_travail(age=25)
fonction_travail()
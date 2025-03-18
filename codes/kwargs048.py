def afficher_kwargs(**kwargs):
    kwargs_copy = kwargs.copy()
    print(kwargs_copy)

afficher_kwargs(a=1, b=2)
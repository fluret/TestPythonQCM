def afficher_kwargs(**kwargs):
    kwargs.clear()
    print(kwargs)

afficher_kwargs(a=1, b=2)
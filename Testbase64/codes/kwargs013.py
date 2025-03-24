def afficher_kwargs(**kwargs):
    print(kwargs.get('c', 'Clé non trouvée'))

afficher_kwargs(a=1, b=2)
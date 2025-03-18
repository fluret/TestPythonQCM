donnees = [1, '2', 3, '4']
resultat = [int(x) for x in donnees if isinstance(x, str)]
print(resultat)
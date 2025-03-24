
mots = ['hello', 'world', 'python']
resultat = [mot for mot in mots if any(c.isupper() for c in mot)]
print(resultat)
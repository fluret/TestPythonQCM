
mots = ['python', 'java', 'ruby']
resultat = [mot for mot in mots if all(c.lower() in 'aeiou' for c in mot)]

print(resultat)
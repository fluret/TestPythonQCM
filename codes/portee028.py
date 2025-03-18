total = 5

def ajouter(total, valeur):
    # Complétez ici
    total += valeur
    return total

print(ajouter(total, 10))

def ajouter_2(valeur):
    global total
    total += valeur
    return total

print(ajouter_2(10))
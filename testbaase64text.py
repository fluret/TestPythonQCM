import base64

# Code Python à encoder (sous forme de chaîne de caractères)
code_python = """
def bonjour():
    print("Salut le monde !")
"""

# Encodage en Base64
encoded_code = base64.b64encode(code_python.encode("utf-8")).decode("utf-8")

# Résultat encodé
print("Code Python encodé en Base64 :")
print(encoded_code)

# Décodage pour vérifier (facultatif)
decoded_code = base64.b64decode(encoded_code).decode("utf-8")
print("\nCode Python décodé :")
print(decoded_code)

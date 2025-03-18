lst = [
    word.upper() if len(word) > 3 else word.lower()
    for word in ["Python", "is", "fun", "to", "learn"]
    if not word.startswith("t")
]

print(lst)
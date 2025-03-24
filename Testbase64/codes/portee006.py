x = 100
def fonction():
    x = 200
    def interne():
        nonlocal x
        x = 300
    interne()
    return x

print(fonction())
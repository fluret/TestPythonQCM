x = 10
def fonction():
    x = 20
    def interne():
        nonlocal x
        x *= 2
    interne()
    return x

print(fonction())
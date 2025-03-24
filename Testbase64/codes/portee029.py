def fonction():
    x = 10
    def interne():
        nonlocal x
        x = 20
    interne()
    print(x)

fonction()
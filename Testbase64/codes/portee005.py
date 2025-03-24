def fonction():
    x = 10
    def interne():
        x = 20
    interne()
    print(x)

fonction()
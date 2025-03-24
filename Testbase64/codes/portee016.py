x = 1
def fonction():
    x = 2
    def interne():
        x = 3
        print(x)
    interne()
    print(x)

fonction()
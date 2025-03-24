x = 5
def fonction():
    print(x)
    def interne():
        print(x)
    x = 10
    interne()

fonction()
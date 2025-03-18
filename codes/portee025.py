x = 5

def fonction():
    x = 10
    def interne():
        print(x)
    interne()

fonction()
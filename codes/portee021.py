x = 10
def fonction():
    x = 20
    def interne():
        print(x)
    x = 30
    interne()

fonction()
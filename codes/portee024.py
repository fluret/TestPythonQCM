x = 10
def fonction():
    y = 20
    def interne():
        z = 30
        print(x, y, z)
    interne()

fonction()
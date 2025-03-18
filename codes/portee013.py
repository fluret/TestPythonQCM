o = 2
def fonction():
    o = 8
    def interne():
        print(o)
    interne()

fonction()
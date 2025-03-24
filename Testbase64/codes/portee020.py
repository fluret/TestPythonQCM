u = 4
def fonction():
    u = 9
    def interne():
        print(u)
    interne()

fonction()
x = 1
def fonction():
    x = 2
    def interne():
        global x
        x = 3
    interne()
    print(x)

fonction()
print(x)
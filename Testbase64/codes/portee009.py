x = 5
def fonction():
    x = 10
    def interne():
        global x
        x = 20
    interne()
    print(x)

fonction()
print(x)
x = 100
def fonction():
    x = 200
    def interne():
        global x
        x = 300
    interne()
    print(x)

fonction()
print(x)
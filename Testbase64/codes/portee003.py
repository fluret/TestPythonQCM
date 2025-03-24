x = 5
def fonction():
    global x
    x = 10
    def interne():
        nonlocal x
        x = 20
    interne()

fonction()
print(x)
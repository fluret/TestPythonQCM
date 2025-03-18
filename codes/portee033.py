def externe():
    x = 5
    def interne():
        x = x + 1
    interne()
    return x

print(externe())
def externe():
    x = 10
    def interne():
        x = 20
    interne()
    return x

print(externe())
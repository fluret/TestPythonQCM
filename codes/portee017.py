s = "globale"
def fonction():
    s = "locale"
    def interne():
        print(s)
    interne()

fonction()
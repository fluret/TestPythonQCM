d = {x: sum(int(digit) for digit in str(x)) for x in range(10) if x % 2 == 0}
print(d)
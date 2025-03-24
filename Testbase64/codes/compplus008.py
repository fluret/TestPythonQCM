divisors_list = [
    (num, [i for i in range(1, num + 1) if num % i == 0])
    for num in range(0, 10)
    if num % 2 == 0
]
print(divisors_list)

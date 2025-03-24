x = 97
my_string = "Start"
while x > 100:
    my_string = my_string + chr(x)
    x = x + 1
else:
    my_string = "42"

print("The answer is " + my_string)
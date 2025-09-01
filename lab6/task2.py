def print_multiples_for(num, count):
    for i in range(1, count + 1):
        print(num * i)
print("Using for loop:")
print_multiples_for(7, 10)
def print_multiples_while(num, count):
    i = 1
    while i <= count:
        print(num * i)
        i += 1
print("Using while loop:")
print_multiples_while(7, 10)

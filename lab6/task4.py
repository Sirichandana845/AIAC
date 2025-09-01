def sum_to_n_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sum_to_n_recursive(n-1)
def sum_to_n_iterative(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
n = 5
print("Recursive:", sum_to_n_recursive(n))
print("For loop:", sum_to_n_iterative(n))
print("While loop:", sum_to_n_while(n))
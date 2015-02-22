def average_a():
    print((3 + 5) / 2)

average_a()

def average_b(a, b):
    print((a + b) / 2)

average_b(3, 5)
average_b(4, 5)

def average_c(a, b):
    return (a + b) / 2

num = average_c(3, 5)
print("The average is " + str(num))

def average_d(a):
    if len(a) == 1:
        a = [a[0], 0]

    sum = 0

    for num in a:
        sum += num

    return sum / len(a)

print(average_d([1, 2, 3, 4]))
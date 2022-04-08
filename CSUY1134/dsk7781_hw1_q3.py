# part a
def square_sum(n):
    total_sum = 0
    for i in range(1, n):
        square = i ** 2
        total_sum += square
    return total_sum


# part b
# n = 3   # n defined here just for sake of tester code in main()
n_square_sum = sum([x**2 for x in range(1, n)])


# part c
def odd_square_sum(n):
    total_sum = 0
    for i in range(1, n, 2):
        square = i ** 2
        total_sum += square
    return total_sum


# part d
# n = 7   # again, n defined for sake of tester code in main()
n_odd_square_sum = sum([x**2 for x in range(1, n, 2)])


def main():  # tester code ONLY
    print(square_sum(4))
    print(n_square_sum)
    print(odd_square_sum(7))
    print(n_odd_square_sum)


# main()  # DO NOT CALL IN SUBMISSION

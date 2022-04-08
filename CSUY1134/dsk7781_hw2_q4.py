def e_approx(n):
    approx_sum = 1
    factorial = 1
    for i in range(n):
        factorial *= i+1  # might break Big Sigma n implementation, but easy
        approx_sum += 1 / factorial
    return approx_sum


def main():  # DO NOT CALL
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)


# main()

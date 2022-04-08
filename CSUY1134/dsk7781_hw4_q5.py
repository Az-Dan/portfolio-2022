# PART A
def count_lowercase(s, low, high):
    # given that low <= high, so no implementation for low > high needed
    index = s[low]
    if low == high:  # stops infinite recursion (?)
        if index.islower():
            return 1  # the 1 letter/index IS lowercase
        else:
            return 0  # the 1 letter/index is NOT lowercase
    next_term = low + 1
    recursive_counting = count_lowercase(s, next_term, high)
    if index.islower():
        return 1 + recursive_counting
    else:
        return recursive_counting


# PART B
def is_number_of_lowercase_even(s, low, high):
    # similar in style to part a, but with some adjustments
    index = s[low]
    lowercase_check = index.islower()
    if low == high:  # stops loop (?) and (hopefully) returns the final verdict (true/false)
        if lowercase_check:
            return False  # 1 is not even
        else:
            return True  # 0 is technically even!
    next_term = low + 1
    recursive_counting = is_number_of_lowercase_even(s, next_term, high)
    if recursive_counting:
        return not lowercase_check  # the two functions swap around each other to mimic even counting
    elif lowercase_check:
        return not recursive_counting
    else:
        return recursive_counting


def main():  # TESTER CODE
    print(is_number_of_lowercase_even('AaAaAaAaAaAaAa', 0, 1))


# main()

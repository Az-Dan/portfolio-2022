def list_min(lst, low, high):
    if low == high:
        return lst[low]
    elif lst[low] < lst[high]:
        prev_value = high - 1  # as in previous value
        return list_min(lst, low, prev_value)  # repeat until one value is narrowed down
    elif lst[low] > lst[high]:
        next_value = low + 1
        return list_min(lst, next_value, high)


def main():  # TESTER CODE
    print(list_min([3, 5, 6, 2, 1, 3, 5, 6, 3, 2], 1, 2))


# main()

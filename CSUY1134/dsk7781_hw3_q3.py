def find_duplicates(lst):
    dup_list = []
    for i in lst:
        if lst[abs(i)] < 0:  # negative = duplicate!
            dup_list.append(abs(i))
        else:
            lst[abs(i)] *= -1  # mark negative/duplicate
    return dup_list
    # no code in place to make sure ints repeated twice don't show up twice, but that might be OK


def main():  # TEST CODE
    print(find_duplicates([1, 2, 2, 1, 4]))


# main()

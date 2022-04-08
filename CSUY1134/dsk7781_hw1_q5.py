def fibs(n):
    curr = 0
    f = 1
    fn = 1
    fi = 0
    while curr < n:  # probably not ideal but uses generator/iterator methods
        curr += 1
        yield f
        fn += fi
        fi = f
        f = fn


def main():  # test code
    for curr in fibs(8):
        print(curr)


# main()

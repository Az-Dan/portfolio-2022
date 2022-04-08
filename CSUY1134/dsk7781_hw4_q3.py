# part a
def print_triangle(n):
    if n == 0:
        return
    else:
        print_triangle(n-1)
        print('*' * n)


# part b
def print_oposite_triangles(n):  # spelled wrong in the question but keeping it for accuracy
    if n == 0:
        return
    print('*' * n)
    print_oposite_triangles(n-1)
    print('*' * n)


# part c
def print_ruler(n):
    if n == 0:
        return
    print_ruler(n-1)
    print('-' * n)
    print_ruler(n-1)

# unfortunately none of the recursions have return statements as in the class/lab examples but that is the only way I could make this work


def main():  # TESTER CODE
    print_ruler(4)


# main()

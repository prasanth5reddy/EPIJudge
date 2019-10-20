from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    # # one line. But takes time and integer overflow might happen
    # return list(map(int, str(int(''.join(map(str, A))) + 1)))

    # Adding digit by digit
    # Time complexity : O(n)
    # Space complexity : O(1)
    c = 1
    for i in reversed(range(len(A))):
        A[i] += c
        if A[i] == 10:
            A[i], c = 0, 1
        else:
            c = 0
            break
    if c:
        # A.insert(0, c)
        A[0] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))

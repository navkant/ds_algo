def reverse_array(arr):
    n = len(arr)
    mid = n // 2
    for i in range(mid):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr


def main(arr, n):
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    x = len(arr) - n
    part1 = reverse_array(arr[:x])
    part2 = reverse_array(arr[x:])
    intermediate = part1 + part2

    print(reverse_array(intermediate))
    return 0


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    print(a)
    main(a, 2)

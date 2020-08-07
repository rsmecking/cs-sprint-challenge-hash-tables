def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    v = []

    for num in a:
        cache[num] = 1
        if num != 0 and -num in cache:
            v.append(abs(num))
    return v


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
#https://www.geeksforgeeks.org/pairs-of-positive-negative-values-in-an-array/
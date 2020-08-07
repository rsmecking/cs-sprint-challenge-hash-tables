
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for i in arrays:
        for num in i:
            if num not in cache:
                cache[num] = result
            else:
                result.append(num)
    result = list(dict.fromkeys(result, 0))
    
 

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
# https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
# https://stackoverflow.com/questions/3869487/how-do-i-create-a-dictionary-with-keys-from-a-list-and-values-defaulting-to-say
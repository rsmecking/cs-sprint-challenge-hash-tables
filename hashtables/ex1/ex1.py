def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for idx, weight in enumerate(weights):
        if weight not in cache:
            cache[weight] = idx

    for num in range(length):
        item_weights = weights[num]
        other_weight = limit - item_weights
        if other_weight in cache and cache[other_weight] != num:
            return(max(num, cache[other_weight]), min(num, cache[other_weight]))
    
    return None

print(get_indices_of_item_weights(weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21))
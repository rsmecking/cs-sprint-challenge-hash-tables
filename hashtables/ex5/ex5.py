# Your code here


cache = {}
result = []
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    
    # Your code here
    for file in files:
        file_name = file.rsplit('/', 1)[1]
        if file_name not in cache:
            cache[file_name] = result
        cache[file_name].append(file)

    for query in queries:
        if query in cache:
            result.extend(cache[query])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
    # result == ['/bin/foo', '/usr/bin/baz'])

# https://www.w3schools.com/python/ref_string_rsplit.asp
# https://www.geeksforgeeks.org/append-extend-python/
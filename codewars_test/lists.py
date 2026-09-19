def array_diff(a, b):
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return result

a = [1, 2, 3]
b = [1, ]
x = array_diff(a, b)
print (x)

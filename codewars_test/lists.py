def array_diff(a, b):
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return result
def solution(text):
    result = []
    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        if len(pair) == 1:
            pair += "_"
        result.append(pair)
    return result

print(solution("jsdjiurbu"))

"""a = [1, 2, 3]
b = [1, ]
x = array_diff(a, b)
print (x)
"""
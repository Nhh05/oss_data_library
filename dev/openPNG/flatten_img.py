def flatten(data):
    result = []
    for item in data:
        if isinstance(item,list):
            result += flatten(item)
        else:
            result.append(item)
    return result

list_1 = [1, [2, [3, 4]], 5,[[[[6]],7]]]
print(flatten(list_1))
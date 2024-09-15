def encodeString(stringVal):
    # Your code goes here.
    count = 0
    result = []
    if not stringVal or len(stringVal) == 0:
        return result
    for i, c in enumerate(stringVal):
        count += 1
        if i > 0:
            if stringVal[i] != stringVal[i - 1]:
                result.append((stringVal[i - 1], count - 1))
                count = 1
    result.append((stringVal[-1], count))
    return result

def decodeString(encodedList):
    # Your code goes here.
    result = ''
    if not encodedList or len(encodedList) == 0:
        return result
    for value, count in encodedList:
        result = result + value * count
    return result

print(encodeString("AAAAABBBBAAA"))
print(decodeString([('W', 5), ('1', 2), ('G', 3)]))
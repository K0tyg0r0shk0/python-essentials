dictionary = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
     'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(input): 
    base = 1
    result = 0
    for letter in input[::-1]:
        value = dictionary.get(letter)
        if value == None:
            return None
        result = result + value * base
        base = base * 16
        
    return result

print(hexToDec('A') == 10)
print(hexToDec('B') == 11)
print(hexToDec('0') == 0)
print(hexToDec('1B') == 27)
print(hexToDec('3C0') == 960)
print(hexToDec('A6G') == None)
print(hexToDec('ZZTOP') == None)
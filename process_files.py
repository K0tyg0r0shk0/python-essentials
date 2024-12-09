
import json

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
            prevChar = char
            count = count + 1
            encodedList.append((prevChar, count))
            return encodedList
        
def decodeString(encodedList):
    decodeStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item [1]
        return decodedStr
    


def encodeFile(filename, newFilename):
    inputFile = open(filename, 'r')
    outputFile = open(newFilename, 'w')
    for line in inputFile.readlines():
        outputFile.write(json.dumps(encodeString(line)))
        outputFile.write('\n')
    outputFile.close()
    inputFile.close()

def decodeFile(filename):
    result = ''
    decodeFile = open(filename, 'r')
    for line in decodeFile.readlines():
        lst = json.loads(line)
        result += decodeString(lst)
    decodeFile.close()
    return result
    
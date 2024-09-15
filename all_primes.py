def allPrimesUpTo(num):
    primesFound = [2]
    for number in range(3, num):
        for prime in primesFound:
            if number % prime == 0:
                break
        else:
            primesFound.append(number)
    return primesFound

print(allPrimesUpTo(100))
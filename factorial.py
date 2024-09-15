def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(5) == 120)
print(factorial(6) == 720)
print(factorial(0) == 1)
print(factorial(-2) == None)
print(factorial(1.2) == None)
print(factorial('Spam Spam Spam') == None)
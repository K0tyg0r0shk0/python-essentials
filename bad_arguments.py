def handleNonIntArguments(func):
    def wrapper(*args):
        for x in args:
            if type(x) != int:
                raise NonIntArgumentException()
        return func (*args)
    
    return wrapper
    
class NonIntArgumentException(Exception):
    pass

@handleNonIntArguments
def sum(a,b,c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print ('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')
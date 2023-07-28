def add(a,b):

    return a+b

def sub(a,b):

    return a-b

def mul(a,b):


    return a*b

def div(a,b):

    try:
        result = a/b
        
    except ZeroDivisionError:
        print("It is not possible to divide by the zero")

    return result
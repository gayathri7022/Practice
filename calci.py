def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def prod(a,b):
    return (a*b)

def div(a,b):
    if b != 0:
        return (a/b)
    else:
        return "ZeroDivisionError"
    

if __name__=='__main__':
    print(add(3,4))

    
    